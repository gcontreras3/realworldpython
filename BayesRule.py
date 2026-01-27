import sys
import random
import itertools
import numpy as np
import cv2 as cv

MAP_FILE = 'cape_python.png'


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