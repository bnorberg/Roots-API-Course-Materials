import cognitive_face as CF
import requests
from io import BytesIO
from PIL import Image, ImageDraw


KEY = '2faaa875087e4266b87ad2c3f18a50cf'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
#img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
img_url = 'https://www.maxpixel.net/static/photo/2x/People-The-Faces-Of-A-Person-Girl-The-Person-Face-369342.jpg'
faces = CF.face.detect(img_url)
print(faces)


def getRectangle(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    return ((left, top), (bottom, right))

def croparea(faceDictionary):
    rect = faceDictionary['faceRectangle']
    left = rect['left']
    top = rect['top']
    bottom = left + rect['height']
    right = top + rect['width']
    return (left, top, bottom, right)

#Download the image from the url
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))

#For each face returned use the face rectangle and draw a red box.
draw = ImageDraw.Draw(img)

f = 0
for face in faces:
    draw.rectangle(getRectangle(face), outline='red')
    crop_img = img.crop(croparea(face))
    f = f+1
    crop_img.save('/Users/brn5/face_crop_{}.png'.format(f))

#Display the image in the users default image browser.
#img.show()
img.save('/Users/brn5/face.png')