from SimpleCV import *

car = Image("sample_data/new-in2.jpg")
no_car = Image("sample_data/new-out3.jpg")

# crop with full car & no back wall:
car = car.crop(170, 170, 230, 300)
no_car = no_car.crop(170, 170, 230, 300)

# used to use 100, 400 (was the worst)
# followed by 50, 200 which was terrible
# used 50, 400 with success
# used 25, 400 with success
# used 300, 400 with success
car = car.edges(25, 400)
no_car = no_car.edges(25, 400)

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

result = car.sideBySide(no_car)
result.show()

car_matrix = car.getNumpy().flatten()
no_car_matrix = no_car.getNumpy().flatten()

car_pixel_count = cv2.countNonZero(car_matrix)
no_car_pixel_count = cv2.countNonZero(no_car_matrix)

print "Car image has " + str(car_pixel_count) + " pixels"
print "No Car image has " + str(no_car_pixel_count) + " pixels"

raw_input()
