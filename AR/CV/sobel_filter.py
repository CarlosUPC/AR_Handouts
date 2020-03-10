import numpy as np
import cv2


def sobel(img):

    img_input = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    img_output = img_input.copy()

    rows = img_input.shape[0]
    columns = img_input.shape[1]

    hd = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]

    for i in np.arange(1, rows - 1):
        for j in np.arange(1, columns - 1):
            neighbors = []
            for k in np.arange(-1, 2):
                for l in np.arange(-1, 2):
                    a = img_input.item(i + k, j + l)
                    neighbors.append(a)
            n = [ [ neighbors[0], neighbors[1],neighbors[2] ], [ neighbors[3],neighbors[4],neighbors[5] ], [neighbors[6],neighbors[7],neighbors[8] ] ]
            gx = np.multiply(hd, n)
            gx = gx.sum()
            img_output.itemset((i,j), gx)
            
    return img_output


def main():
    img_output = sobel('img/sonic.jpg')

    cv2.imwrite('img/sonic_sobel.jpg', img_output)
    cv2.imshow('Sobel Filter', img_output)
    cv2.waitKey(0)
    


main()


