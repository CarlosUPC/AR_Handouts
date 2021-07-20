import numpy as np
import cv2

def gaussianKernel(krad):

    

    #kernel
    ksize = (2 * krad) + 1
    krn = np.zeros((ksize, ksize))
   ## krn[:, :] = 1.0 / (ksize * ksize)

    #gaussian

    for i in range(0, ksize):
        for j in range(0, ksize):
            d = np.sqrt(((krad-i)**2) + ((krad-j)**2))
            sigma = krad / 3
            krn[i,j] = np.exp(-((d**2) / (2* sigma**2)))

    krn /= krn.sum()
    return krn

def main():
    krn = gaussianKernel(100)
    cv2.imshow("Gaussian Kernel", krn*100000)
    cv2.waitKey(0)

main()
