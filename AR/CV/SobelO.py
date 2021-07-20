import cv2 as cv2
import numpy as np

def boxFilter(img):
    img = img/255.0

    #kernel
    ksize = 11
    krn = np.zeros((ksize,ksize))
    krn[:,:] = 1.0/(ksize*ksize)

    #filter
    filtered = convolve(img,krn)
    return filtered

def convolve(img,krn):
    ksize, _ = krn.shape
    krad = int(ksize/2)

    height, width, depth = img.shape
    framed = np.ones((height + 2*krad, width + 2*krad, depth))
    framed[krad:-krad,krad:-krad] = img
    
    #filter

    filtered = np.zeros(img.shape)
    for i in range(0,height):
        for j in range(0,width):
            filtered[i,j] = (framed[i:i+ksize, j:j+ksize] * krn[:,:, np.newaxis]).sum(axis=(0,1))

    return filtered

def SobelFilter(img):
    img = img/255.0

    h_image = convolve(img,np.array([[-1,0,1], [-2,0,2],[-1,0,1]]))

    v_image = convolve(img,np.array([[-1,-2,-1], [0,0,0],[1,2,1]]))

    return np.sqrt(h_image**2 + v_image**2)
    
def CannyFromSobel(img):
    krad = 3
    height, width, depth = img.shape
    framed = np.ones((height + 2*krad, width + 2*krad, depth))
    framed[krad:-krad,krad:-krad] = img
    
    #filter
    filtered = np.zeros(img.shape)
    max_val = 0
    for i in range(0,height):
        for j in range(0,width):
           max_val = np.amax(framed[i:i+1, j:j+1])
            for z in range(0,3):
                for k in range(0,3):
                    if(framed[z,k] == max_val):
                        filtered[i,j] = 1
                    else:
                        filtered[i,j] = 0
return filtered
    
img = cv2.imread("h_knight.jpg")

final_image = SobelFilter(img)
cannyImage_filter = CannyFromSobel(final_image)
cv2.imwrite("canny_filter.jpg", cannyImage_filter)
cv2.imshow("canny_filter.jpg",cannyImage_filter)

cv2.waitKey(0)