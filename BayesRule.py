# Importing modules - Python standard library, third party modules, user defined modules
import sys # Includes commands for the operating system, such as exiting.
import random # Includes commands for generating random numbers. In this case, pseudorandom numbers.
import itertools # Includes commands for creating and using iterators for efficient looping.
import numpy as np
import cv2 as cv

# OpenCV will define each rectangle by the pixel number at the corner points.
# Assign a variable to each corner point for each sampling area.
# The order of the corner points is: (Upper Left X, Upper Left Y, Lower Right X, Lower Right Y)
MAP_FILE = 'cape_python.png'
# SA - Represents Search Area
SA1_CORNERS = (130, 265, 180, 315) # (UL-X, UL-Y, LR-X, LR-Y)
SA2_CORNERS = (80, 255, 130, 305)  # (UL-X, UL-Y, LR-X, LR-Y)
SA3_CORNERS = (105, 205, 155, 255) # (UL-X, UL-Y, LR-X, LR-Y)

class Search():
    """Bayesian Search & Rescue game with 3 search areas."""

    def __init__(self, name):
        self.name = name
        self.img = cv.imread(MAP_FILE, cv.IMREAD_COLOR)
        if self.img is None:
            print('Could not load map file {}'.format(MAP_FILE),
            file=sys.stderr)
            sys.exit(1)

        self.area_actual = 0
        self.sailor_actual = [0, 0] # As "local" coords within search area

        # these are showing the Y, X coords within the image

        self.sa1 = self.img[SA1_CORNERS[1] : SA1_CORNERS[3], SA1_CORNERS[0] : SA1_CORNERS[2]]
        self.sa2 = self.img[SA2_CORNERS[1] : SA2_CORNERS[3], SA2_CORNERS[0] : SA2_CORNERS[2]]
        self.sa3 = self.img[SA3_CORNERS[1] : SA3_CORNERS[3], SA3_CORNERS[0] : SA3_CORNERS[2]]

        self.p1 = 0.2
        self.p2 = 0.5
        self.p3 = 0.3

        self.sep1 = 0
        self.sep2 = 0
        self.sep3 = 0

def draw_map(self, last_known):
    """Display basemap with scale, last known [x, y] location, search areas."""
    cv.line(self.img, (20, 270), (70, 370), (0, 0, 0), 2) # Scale bar using line() method pass base map image, a tuple of the left end point, a tuple of the right end point, a tuple of the color in BGR format, and the thickness of the line.
    cv.putText(self.img, '0', (8, 370), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0)) # putText() method to annotate the scale bar, passing the attriute for the base map image, the text to display, a tuple for the bottom-left corner of the text, the font type, font scale, and color in BGR format.
    cv.putText(self.img, '50 Nautical Miles', (71, 370), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))

    cv.rectangle(self.img, (SA1_CORNERS[0], SA1_CORNERS[1]), (SA1_CORNERS[2], SA1_CORNERS[3]), (0, 0, 0), 1)
    
    cv.putText(self.img, '1', (SA1_CORNERS[0] + 3, SA1_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0)

    cv.rectangle(self.img, (SA2_CORNERS[0], SA2_CORNERS[1]), (SA2_CORNERS[2],  SA2_CORNERS[3]), (0, 0 , 0), 1)

    cv.putText(self.img, '2', (SA2_CORNERS[0] + 3, SA2_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0)

    cv.rectangle(self.img, (SA3_CORNERS[0], SA3_CORNERS[1]), (SA3_CORNERS[2], SA3_CORNERS[3]), (0, 0, 0), 1)
    cv.putText(self.img, '3', (SA3_CORNERS[0] + 3, SA3_CORNERS[1] + 15), cv.FONT_HERSHEY_PLAIN, 1, 0)

    cv.putText(self.img, '+', (last_known), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
    cv.putText(self.img, '+ = Last Known Position', (274, 355), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))

    cv.putText(self.img, '* = Actual Position', (275, 370), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 0))
    
    cv.imshow('Search Area', self.img)
    cv.moveWindow('Search Area', 750, 10)
    cv.waitKey(500)

# def bayes_rule(prior, likelihood, evidence):
#     """
#     Calculate the posterior probability using Bayes' Rule.

#     Parameters:
#     prior (float): Prior probability of the hypothesis.
#     likelihood (float): Likelihood of the evidence given the hypothesis.
#     evidence (float): Total probability of the evidence.

#     Returns:
#     float: Posterior probability of the hypothesis given the evidence.
#     """
#     return (likelihood * prior) / evidence