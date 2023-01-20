from distutils.core import setup # Need this to handle modules
import py2exe 
import pygame, sys, time
from pygame.locals import *
from random import randint
from pygame import mixer

setup(console=['Menu.py']) # Calls setup function to indicate that we're dealing with a single console application