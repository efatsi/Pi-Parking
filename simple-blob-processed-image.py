from SimpleCV import *

img = Image("sample_data/out1.jpg")

img = img.binarize(150)

blobs = img.findBlobs()

if blobs:
    blobs = blobs.filter(blobs.area() > 50)
    blobs.draw(width=5)

img.show()
raw_input()
