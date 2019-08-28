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