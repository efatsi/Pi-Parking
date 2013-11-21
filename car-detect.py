from SimpleCV import *

#img = Image("screenshots/sample_data/new-out1.jpg")

car = Image("screenshots/sample_data/new-in2.jpg")
no_car = Image("screenshots/sample_data/new-out3.jpg")

#img = img.crop(195, 190, 185, 140)
#img = img.crop(170, 170, 230, 300)

#car = car.crop(195, 195, 185, 140)
#no_car = no_car.crop(195, 190, 185, 140)

# crop with full car & no back wall:
car = car.crop(170, 170, 230, 300)
no_car = no_car.crop(170, 170, 230, 300)

# used to use 100, 400 (was the worst)
# followed by 50, 200 which was terrible
# used 50, 400 with success
# used 25, 400 with success

#car = car.edges(300, 400)
#no_car = no_car.edges(300, 400)

car = car.edges(25, 400)
no_car = no_car.edges(25, 400)

# FILTER!
#car.dl().polygon([(230, 140), (230, 300), (0, 300)], filled=True, color=Color.BLACK) 
#no_car.dl().polygon([(230, 140), (230, 300), (0, 300)], filled=True, color=Color.BLACK) 

#car.dl().polygon([(0, 0), (), ()]

#car = car.applyLayers()
#no_car = no_car.applyLayers()

# make MASK!
mask = Image(car.size())
dl = DrawingLayer(car.size())
# get rid of bushes
dl.polygon([(230, 100), (230, 300), (0, 300), (0, 260)], filled=True, color=Color.WHITE)
# get rid of brick wall
dl.polygon([(0, 0), (35, 0), (10, 300), (0, 300)], filled=True, color=Color.WHITE)
# get rid of back of car
dl.polygon([(115, 0), (230, 0), (230, 300), (115, 300)], filled=True, color=Color.WHITE)
mask.addDrawingLayer(dl)
mask = mask.applyLayers()

car = car - mask
no_car = no_car - mask

#points = [(10,10),(30,20),(50,10),(40,50),(10,40)]
#car = car.dl().polygon(points, filled=True, color=Color.RED)

#canny1 = img.edges(100, 400)
#canny2 = img.edges(300, 400)

#blobs = img.findBlobs(minsize=400, maxsize=100000)

#for blob in blobs:
#    blob.drawMinRect(color=Color.RED, width=2)

#img.show()

#canny_blobs = canny1.findBlobs()

#canny_blobs = canny_blobs.filter(canny_blobs.area() > 50)
#for blob in canny_blobs:
#    blob.drawMinRect(color=Color.RED, width=2)

#canny1.show()

#result = canny1.sideBySide(canny2)
result = car.sideBySide(no_car)
result.show()

car_matrix = car.getNumpy().flatten()
no_car_matrix = no_car.getNumpy().flatten()

car_pixel_count = cv2.countNonZero(car_matrix)
no_car_pixel_count = cv2.countNonZero(no_car_matrix)

print "Car image has " + str(car_pixel_count) + " pixels"
print "No Car image has " + str(no_car_pixel_count) + " pixels"

#img.show()
raw_input()
