import cv2 as cv

img = cv.imread("/Users/zdeno/Desktop/karlik.png", cv.IMREAD_COLOR)

if img is None:
    print("Error: Could not read the image.")
else:
    resized_img = cv.resize(img, (400, 400))
    cv.imshow("window_name", resized_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite("image.jpg", resized_img)