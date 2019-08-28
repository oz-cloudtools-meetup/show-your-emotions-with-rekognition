# Show your emotions with Rekognition

## Steps 1
 - Install dependencies
 - Create an S3 bucket to store the image to be used in next steps
 - Create a rekognition collection to store the facial signature
```bash
# Install dependencies
./setup.sh

# Create your s3 bucket, pick a globally unique bucket name
aws s3 mb s3://<your bucket name>

# Create a rekognition pool
aws rekognition create-collection --collection-id "aws-meetup"
```
## Steps 2
 - Ready a photo and save it onto your local machine, make sure there is at lease one face in it
 - Upload it to your Cloud9 IDE working directory
 ```bash
# In case the Cloud9 'Upload Local Files" doesn't work, follow the steps below:
# - Run 'convertImageBase64.py' against the image file 
# - in Cloud9 run 'assembleImg.py' against the base64 file obtained from last step
```
## Steps 3
 - Modify the variables in index.py
```bash
python3 index.py
```
 - AWS rekognition returns the metadata of the face
 - As we set "MaxFaces = 1", rekognition only return metadata about the most prominent face

## Steps 4
 - Generate a signed url for users without aws credentials to temporarily access the image
 - Modify the variables in url_gen.py
```bash
python3 url_gen.py
```
 - Copy the url prompted on console and paste it to your browser