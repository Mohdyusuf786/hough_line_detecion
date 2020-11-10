# canny edge detection
# mapping of edge points to the hough space and storage in the accumulator
# interpretation of the accumulator to yield lines of infinite length. the interpretation can be done by thresholding ans possibly other constraints
# conversion of infinite line to finite lines

import cv2
import numpy as np

img = cv2.imread('window.png')
img = cv2.resize(img, (500, 500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 150, 150, apertureSize=5)
cv2.imshow("edge", canny)
# lets try standand hough line detection
lines = cv2.HoughLines(canny, 1, np.pi / 180, 165)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)

    x0 = a * rho
    y0 = b * rho

    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))

    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("Hough lines", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
