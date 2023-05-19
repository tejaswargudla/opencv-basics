import cv2 as cv
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-i","--image",required=True,help="Image name or path of the image")
ap.add_argument("-o","--output_filename",required=True,help = "Output filename to write")
args = vars(ap.parse_args())
image = cv.imread(args['image'])
(h,w,c) = image.shape[:3]

print("Height of the image",h)
print("Width of the image",w)
print("Channels of the image",c)

cv.imshow("Image Show",image)
cv.waitKey(0)

cv.imwrite(args['output_filename'],image)