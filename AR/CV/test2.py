import numpy as np
import cv2


def main():
    original = cv2.imread("img/lena_noise.png", 0)
    cv2.imshow("Original", original)
    cv2.waitKey(0)

main()