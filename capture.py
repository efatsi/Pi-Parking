import pygame
import pygame.camera
from pygame.locals import *
from datetime import datetime

pygame.init()
pygame.camera.init()

cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
image = cam.get_image()

fileName = "screenshot_" + datetime.now().strftime("%m-%d_%H:%M")

pygame.image.save(image, fileName)

