import cv2

img = cv2.imread('dqn.png')
img1 = img[41:257, 457:830]
cv2.imshow('image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

print img.shape