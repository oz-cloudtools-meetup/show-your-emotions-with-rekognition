#!/usr/bin/python3
# Generate a presigned URL for the S3 object
import logging
import boto3
import argparse
from botocore.exceptions import ClientError

BUCKET = ""
PROCESSED_IMAGE = ""

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help = 'name of processed image')
ap.add_argument('-b', '--bucket', required=True, help = 'your bucket name')
args = ap.parse_args()
if (args.image != None):
    PROCESSED_IMAGE = args.image 
if (args.bucket != None):
    BUCKET = args.bucket 

def create_presigned_url(bucket_name, object_name, expiration=3600):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': object_name}, ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None
    return response

if __name__=='__main__':
    # Generate a signed url to access the image
    print("\nUse the url below to access the processed image: ")
    print(create_presigned_url(BUCKET, PROCESSED_IMAGE, expiration=3600))
