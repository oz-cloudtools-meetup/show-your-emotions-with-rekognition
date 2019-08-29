# Show your emotions with Rekognition
<!-- TODO -->
<!-- Elaboration about the aws services used here S3 Rekognition Lambda -->
## Steps 1 - Basic preparation
 - Install dependencies. Libraries we need are included in setup.sh. Run it to install.
 - Create an aws S3 bucket to store the image to be used in next steps. This bucket is also used to store processed image and enable a signed url to allow temporary access to the image from a user who doesn't have aws credentials. 
 - Create a rekognition collection to store the facial signature. A facial signature consists of feature vectors sampled by aws rekognition service from input image frame and this metadata can be used for matching faces and emotioanl analysis. AWS rekognition service groups the signatures about objects including faces into collections. 
```bash
# Install dependencies
# Make sure the console outputs "Dependencies installed successfully." 
./setup.sh

# Create your s3 bucket using command below, pick a globally unique bucket name. This bucket name will be used in next steps
# If successful, console will prompt: "make_bucket:<your bucket name>"
# Use command  'aws s3 ls' to verify the creation of bucket
aws s3 mb s3://<your_bucket_name>

# Create a rekognition pool 
# Console will prompt "StatusCode": 200 when successful
aws rekognition create-collection --collection-id <your_collection_name>

# Clone the github repo
git clone <repo>
```

## Steps 2 - Upload an image to S3 bucket
 - Ready a photo and save it onto your local machine, make sure there is at lease one face in it. AWS rekognition service can index up to 100 faces at once, here we keep it simple by letting rekognition index the one prominent face. Detail shown in step 3.
 - Upload it to your Cloud9 IDE working directory: same directory where .py files resides
 ```bash
# In case the Cloud9 'Upload Local Files" doesn't work, follow the steps below:
# - Run 'convertImageBase64.py' against the image file 
# - in Cloud9 run 'assembleImg.py' against the base64 file obtained from last step
```

## Steps 3 - Create a lambda function to index the image we put to S3 
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