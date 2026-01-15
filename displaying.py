import cv2

image = cv2.imread("images.jpg")

if image is not None:
   
   grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   cv2.imshow("Original Image", image)
   
   resize = cv2.resize(grey,(300,300))
   cv2.imshow("Resized Image", resize)

   slices = image[100:200,30:140]
   cv2.imshow("Cropped", slices)

   cv2.waitKey(0)
   cv2.destroyAllWindows()

   cv2.imwrite("grey.jpg", grey)
   cv2.imwrite("resize.jpg", resize)
   cv2.imwrite("sliced.jpg", slices)

    
else :
    print("Could Not load the image")   


