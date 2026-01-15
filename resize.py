import cv2

image = cv2.imread("images.jpg")

pt1 = (100,50)
pt2 = (200,100)
colour = (0,255,10)

lined = cv2.line(image, pt1,pt2, colour, thickness= 2)
resized = cv2.resize(image, (100,100))
cv2.imshow("Liend image", lined)
cv2.imshow("Resized Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("lined.jpg", lined)
cv2.imwrite("resized.jpg", resized)
print(image.shape)