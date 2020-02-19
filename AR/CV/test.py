import numpy as np
import cv2


def ex1():
    vec = np.zeros(10)
    print(vec)


def ex2():
    vec = np.zeros(10)
    vec[4] = 1
    print(vec) 

def ex3():
    vec = np.arange(10,50)
    print(vec)



def ex4():
    arr = np.arange(0.0, 9.0) 
    arr = arr.reshape((3, 3))
    print(arr)

def ex5():
    arr = np.arange(0.0, 9.0) 
    arr = arr.reshape((3, 3))
    arr = np.fliplr(arr)
    print(arr)

ex5()

