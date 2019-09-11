import json
import cv2
import boto3

def lambda_handler(event, context):
    # Fetch event trigger information
    BUCKET = event['Records'][0]['s3']['bucket']['name']
    IMAGE = event['Records'][0]['s3']['object']['key']
    PROCESSED_BUCKET = "<YOUR_PROCESSED_BUCKET>" # e.g. rekognition-workshop-processed
    
    # Modify variable names here
    COLLECTION = "<your_collection>" # e.g. rekognition-workshop-simon
    PROCESSED_IMAGE = "<you_name_the_processed_image>" # e.g. processed_image.jpg
    
    # Create an s3 client 's3' and then send this image to the s3 bucket
    s3 = boto3.resource('s3')
    
    # Create a rekognition client 'reko'
    reko = boto3.client('rekognition')
    
    # Index the face and receive response from rekognition service
    response = reko.index_faces(
        CollectionId = COLLECTION,
        Image = {
            'S3Object': {
                'Bucket': BUCKET,
                'Name': IMAGE
            }
        },
        DetectionAttributes = ['ALL']
        # MaxFaces = 1,
        # QualityFilter = 'AUTO'
    )
    
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
    localPath = "/tmp/" + IMAGE
    s3.meta.client.download_file(BUCKET, IMAGE, localPath)
    img = cv2.imread(localPath, 1)
    imgHeight, imgWidth, channels = img.shape

    # Draw on the image 
    box = info['BoundingBox']
    left = int(imgWidth * box['Left'])
    top = int(imgHeight * box['Top'])
    width = int(imgWidth * box['Width']) + left
    height = int(imgHeight * box['Height']) + top
    cv2.rectangle(img, (left, top), (width, height), (0, 255, 0), 2)
    # cv2.putText(img, str(emotion), (50, 50), FONT, 1, (0, 255, 0), 2, cv2.LINE_AA)
    
    # Save this image and send it to s3
    tempPath = "/tmp/" + PROCESSED_IMAGE
    cv2.imwrite(tempPath, img)
    s3.meta.client.upload_file(tempPath, PROCESSED_BUCKET, PROCESSED_IMAGE)
