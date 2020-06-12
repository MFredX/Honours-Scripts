# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 00:20:45 2020

@author: sachi
"""

from PIL import *
import numpy as np
from pylab import *

#matplotlib inline  

#Import an image
#image = Image.open('./Training/croppedDrive.jpg')
image = Image.open('./Training/frameNumbers13.jpg')

#image.show()

im = image.convert('L')
#im.show()

a = np.asarray(im)

# create a new figure
figure()
gray()
# show contours with origin upper left corner
contour(im, origin='image')
axis('equal')
axis('off')


figure()


hist(a.flatten(), 128)

show()