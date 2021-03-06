#!/usr/bin/python3
import cv2
import boto3

# Modify varible names here
BUCKET = "<YOUR_BUCKET>" # e.g. rekognition-workshop
IMAGE = "<YOUR_IMAGE>"  # e.g. raw_image.jpg
COLLECTION = "<YOUR_COLLECTION>" # e.g. rekognition-workshop
PROCESSED_IMAGE = "<YOUR_PROCESSED_IMAGE>" # e.g. processed_image.jpg

if __name__=='__main__':

    # Create an s3 client 's3' and a rekognition client 'reko'
    s3 = boto3.resource('s3') 
    reko = boto3.client('rekognition') 

    # Index the face and receive response from rekognition service
    response = reko.index_faces(
        CollectionId = COLLECTION,
        Image = {
            'S3Object': {
                'Bucket': BUCKET,
                'Name': IMAGE,
            }
        },
        DetectionAttributes = ['ALL'],
        MaxFaces = 1,
        QualityFilter = 'AUTO'
    )
    # print(response)

    # Extract face metadata from the response
    info = response['FaceRecords'][0]['FaceDetail']
    smileConfidence = info['Smile']['Confidence']
    smile = info['Smile']['Value']
    gender = info['Gender']['Value']
    agelow = info['AgeRange']['Low']
    agehigh = info['AgeRange']['High']
    faceId = response['FaceRecords'][0]['Face']['FaceId']

    # Determine emotion by picking the one with highest confidence
    emotions = info['Emotions']
    emotionType = []
    emotionConf = []
    count = 0
    for allEmotions in emotions:
        emotionType.insert(count, allEmotions['Type'])
        emotionConf.insert(count, allEmotions['Confidence'])
        count += 1
    max_value = max(emotionConf)
    max_index = emotionConf.index(max_value)
    emotion = emotionType[max_index]

    print("Information about face ID " + str(faceId) + ":")
    print("Smile: " + str(smile) + "\nThe confidence is: " + str(smileConfidence))
    print("Gender: " + str(gender))
    print("Age between: " + str(agelow) + " to " + str(agehigh))
    print("Emotion: " + str(emotion))

    # Get the image W x H 
    img = cv2.imread(IMAGE,1)
    imgHeight, imgWidth, channels= img.shape

    # Get bounding box values and turn it into drawing coordinates
    box = info['BoundingBox']
    left = int(imgWidth * box['Left'])
    top = int(imgHeight * box['Top'])
    width = int(imgWidth * box['Width']) + left
    height = int(imgHeight * box['Height']) + top

    # Draw on the image
    cv2.rectangle(img, (left, top), (width, height), (0, 255, 0), 2)

    # Save this image and send it to s3
    cv2.imwrite(PROCESSED_IMAGE, img)
    s3.meta.client.upload_file(PROCESSED_IMAGE, BUCKET, PROCESSED_IMAGE)
