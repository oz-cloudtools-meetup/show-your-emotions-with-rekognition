#!/usr/bin/python3
import boto3

# Modify varible names here
BUCKET = "<YOUR_BUCKET>"
IMAGE = "<YOUR_IMAGE>"

# Create an s3 client 's3' 
s3 = boto3.resource('s3')

# Use s3 client to send this image to the s3 bucket
s3.meta.client.upload_file(IMAGE, BUCKET, IMAGE)