from SimpleCV import *

car = Image("sample_data/new-in2.jpg")
no_car = Image("sample_data/new-out3.jpg")

# crop with full car & no back wall:
car = car.crop(170, 170, 230, 300)
no_car = no_car.crop(170, 170, 230, 300)

blobs = car.findBlobs(minsize=400, maxsize=100000)
for blob in blobs:
    blob.drawMinRect(color=Color.RED, width=2)
#car.show()

blobs = no_car.findBlobs(minsize=400, maxsize=1000000)
for blob in blobs:
    blob.drawMinRect(color=Color.RED, width=2)
no_car.show()

raw_input()
