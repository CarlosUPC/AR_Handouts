import numpy as np
import cv2



def medianFilter(img):

    img_input = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    img_output = img_input.copy()

    rows = img_input.shape[0]
    columns = img_input.shape[1]

    for i in np.arange(3, rows - 3):
        for j in np.arange(3, columns - 3 ):
            neighbors = []
            for k in np.arange(-3, 4):
                for l in np.arange(-3, 4):
                    a = img_input.item(i + k, j + l)
                    neighbors.append(a)
            neighbors.sort()
            median = np.median(neighbors)
            b = median
            img_output.itemset((i,j), b)

    return img_output


def main():
    img_output = medianFilter('img/lena_noise.png')

    cv2.imwrite('img/lena_median.jpg', img_output)
    cv2.imshow('Median Filter', img_output)
    cv2.waitKey(0)
    


main()
