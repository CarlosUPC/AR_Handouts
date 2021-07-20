
import cv2 as cv2
import numpy as np



def erosion(img, kernel):
	lena_erosion = np.zeros(img.shape, dtype=np.int)
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			if(img[i][j]>0):
				fit = True
				min_pixel = 255
				for k, l in kernel:
					if ((i+k)<0 or (j+l)<0 or (i+k)>=img.shape[0] or (j+l)>=img.shape[1] or img[i+k][j+l]==0):
						fit = False
						break
				if fit:
					for k, l in kernel:
						min_pixel = img[i+k][j+l] if img[i+k][j+l] < min_pixel else min_pixel
					lena_erosion[i][j] = min_pixel;
	return lena_erosion



    def main():

        kernel = [			  [-2, -1], [-2, 0], [-2, 1],
                    [-1, -2], [-1, -1], [-1, 0], [-1, 1], [-1, 2],
                    [ 0, -2], [ 0, -1], [ 0, 0], [ 0, 1], [ 0, 2],
                    [ 1, -2], [ 1, -1], [ 1, 0], [ 1, 1], [ 1, 2],
                            [ 2, -1], [ 2, 0], [ 2, 1]
                ]

        img = cv2.imread('C:\Users\wolfs\Documents\GitHub\AR_Handouts\AR\CV\img\morphology.png', 0)
        lena_erosion = erosion(img, kernel)
        cv2.imwrite('C:\Users\wolfs\Documents\GitHub\AR_Handouts\AR\CV\img\morphology_erosion.png',lena_erosion)



    main()