from SimpleCV import Camera

# Initialize the camera
cam = Camera()

# Loop to continuously get images
while True:
    # Get Image from camera
    initial_img = cam.getImage()

    # Binarized
    img = initial_img.binarize(150)

    print "hey"

    # Blobs
    blobs = img.findBlobs()

    if blobs:
        blobs = blobs.filter(blobs.area() > 50)
        blobs.draw(width=5)

    # Show the image
    img.show()

