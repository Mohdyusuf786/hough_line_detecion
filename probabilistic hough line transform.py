import cv2
import numpy as np

img = cv2.imread('window.png')
img = cv2.resize(img, (600, 500))
cv2.imshow("org", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150, apertureSize=5)
cv2.imshow("edge", canny)
# lets try probabilistic hough line transform
lines = cv2.HoughLinesP(canny, 1, np.pi / 180, 100, minLineLength=220, maxLineGap=7)
for line in lines:
    x1, y1, x2, y2 = line[0]

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv2.imshow("Hough lines", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
