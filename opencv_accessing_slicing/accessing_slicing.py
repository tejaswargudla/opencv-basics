import cv2 as cv
import argparse

ap = argparse.ArgumentParser()

ap.add_argument('-i','--image', default='inputImage.jpg',help = 'Image filename')

args = vars(ap.parse_args())

image = cv.imread(args['image'])

h,w = image.shape[:2]

cv.imshow("Input Image",image)
cv.waitKey(0)

(b,g,r) = image[20,50]

print("Blue Value:{}, Green Value:{}, Red value:{}".format(b,g,r))

image[20,50] = (0,0,255)

(b_n,g_n,r_n) = image[20,50]
print("New Blue Value:{}, New Green Value:{}, New Red value:{}".format(b_n,g_n,r_n))


c_x,c_y = w//2,h//2

top_left = image[0:c_y,0:c_x]
top_right = image[0:c_y,c_x:w]
bottom_left = image[c_y:h,0:c_x]
bottom_right = image[c_y:h,c_x:w]
# bottom_right = 
cv.imshow("Top Left",top_left)
cv.imshow("Top Right",top_right)
cv.imshow("Bottom Left",bottom_left)
cv.imshow("Bottom Right",bottom_right)
cv.waitKey(0)