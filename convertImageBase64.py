# Due to s3 blocked, convert an image into base64 so it can be copy paste somewhere else 
import base64

# Choose an image
IMAGE_PATH = "<path_to_the_image>"
ENCODING="utf-8"

with open(IMAGE_PATH, "rb") as image_file:    
    encoded_string = base64.b64encode(image_file.read())
    b64_string = encoded_string.decode(ENCODING)
    print(b64_string)
    
print("\nPlease copy the string above into designated place in assembleImg.py manually")