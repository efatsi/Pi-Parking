from SimpleCV import *
import sys
import requests
import json

if len(sys.argv) > 1:
  image_string = sys.argv[1]
else:
  image_string = "sample_data/new-in2.jpg"
image = Image(image_string)

# crop with full car & no back wall:
image = image.crop(170, 170, 230, 300)

# used to use 100, 400 (was the worst)
# followed by 50, 200 which was terrible
# used 50, 400 with success
# used 25, 400 with success
# used 300, 400 with success
image = image.edges(25, 400)

# make MASK!
mask = Image(image.size())
dl = DrawingLayer(image.size())
# get rid of bushes
dl.polygon([(230, 100), (230, 300), (0, 300), (0, 200)], filled=True, color=Color.WHITE)
# get rid of brick wall
dl.polygon([(0, 0), (35, 0), (10, 300), (0, 300)], filled=True, color=Color.WHITE)
# get rid of back of car
#dl.polygon([(115, 0), (230, 0), (230, 300), (115, 300)], filled=True, color=Color.WHITE)
mask.addDrawingLayer(dl)
mask = mask.applyLayers()

image = image - mask

#image.show()

image_matrix = image.getNumpy().flatten()

image_pixel_count = cv2.countNonZero(image_matrix)

#print "Image " + image_string + " has " + str(image_pixel_count) + " pixels"

url = "http://pi-parking.herokuapp.com/updates"
files = {'update[image]': (image_string, open(image_string, 'rb'))}
#headers = {'content-type': 'image/png'}

if image_pixel_count > 4000:
  print "TAKEN"
  status = {'update[status]': 'taken'}
else:
  print "AVAILABLE"
  status = {'update[status]': 'available'}

#r = requests.post(url, data=status, files=files, headers=headers)
r = requests.post(url, data=status, files=files)
print r.text

#raw_input()
