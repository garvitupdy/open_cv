import cv2

image = cv2.imread("images.jpg")
if image is not None: 
    h,w = image.shape[:2]

    center_point = (w//2, h//2)

    m = cv2.getRotationMatrix2D(center_point, 90, 0.5)
    rotated = cv2.warpAffine(image, m , (w,h))
    flipped_horizontally = cv2.flip(image, 1)
    flipped_vertically = cv2.flip(image,0)
    flipped_both = cv2.flip(image, -1)

    cv2.imshow("original", image)
    cv2.imshow("Rotated Image", rotated)
    cv2.imshow("Horizontal", flipped_horizontally)
    cv2.imshow("Vertical", flipped_vertically)
    cv2.imshow("Both", flipped_both)
    

    cv2.imwrite("rotated.jpg", rotated)
    cv2.imwrite("Horizontal.jpg", flipped_horizontally)
    cv2.imwrite("Vertical.jpg", flipped_vertically)
    cv2.imwrite("Flipped_both.jpg", flipped_both)

    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")