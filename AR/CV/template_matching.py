import numpy as np
import cv2

original = cv2.imread('assets/img2.png', cv2.IMREAD_COLOR)
temporal = cv2.imread('assets/img2.png',0) 
target = cv2.imread('assets/t1-img2.png',0) 

cv2.imshow("Original", temporal)

threshold = 0.1

originalHeight, originalWidth = temporal.shape
targetHeight, targetWidth = target.shape

matchingMap = np.zeros((originalHeight - targetHeight + 1, originalWidth - targetWidth + 1))

for y in range(0, originalHeight - targetHeight + 1):
    for x in range(0, originalWidth - targetWidth + 1):
        for ty in range(0, targetHeight):
            for tx in range(0, targetWidth):
                matchingMap[y, x] += (target[ty, tx] - temporal[y + ty, x + tx])**2


matchingMap = matchingMap / matchingMap.max()
matches = np.where(matchingMap <= threshold)

for match in zip(*matches[::-1]):
    cv2.rectangle(original, match, (match[0] + targetWidth, match[1] + targetHeight), (0, 255, 0), 2)

cv2.imshow("Original", original)
cv2.imshow("Matching Map", matchingMap)

k = cv2.waitKey(0)

if k == 27:
    # Wait for ESC key to quit all windows
    cv2.destroyAllWindows()