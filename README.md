# Show your emotions with Rekognition

## Steps 1
 - Install dependencies.
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
