# Used to bypass s3 blockage at nab
import base64
from PIL import Image
from io import BytesIO

"""
MODIFICATION NEEDED:
Paste the base64 string you got from running convertImageBase64.py
to replace anything between the triple single quote below
"""
data = b'''<the base64 string>'''

im = Image.open(BytesIO(base64.b64decode(data)))
# Image file name below will be used in next steps
im.save('<image_file_name.jpg>', 'JPEG')