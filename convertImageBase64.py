# Due to s3 blocked, convert an image into base64 so it can be copy paste somewhere else 
import base64

# Choose an image
IMAGE_PATH = "/Users/p784719/Downloads/<the_image>"
ENCODING="utf-8"

with open(IMAGE_PATH, "rb") as image_file:    
    encoded_string = base64.b64encode(image_file.read())
    b64_string = encoded_string.decode(ENCODING)
    # payload = {"image_key": b64_string, "filename": imageFile}
    # response = requests.post(INVOKEURL, data=json.dumps(payload))
    print(b64_string)
    
# Manually copy the string into 'assembleImg.py'