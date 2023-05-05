import cv2

# for reading the image
src = cv2.imread("6.jpg", cv2.IMREAD_UNCHANGED)

# percentage by which you want to reduce image to

scale_per = 100- int(input('How much percentage you want to reduce your image (in %) = '))

# calcularing the height and width of the emage after reduction
# shape[0] -> height
# shape[1] -> width
new_width = int(src.shape[1] * scale_per /100)
new_height = int(src.shape[0] * scale_per /100)

# resizing the image and storing it as a new file
dsize = (new_width, new_height)
res_img = cv2.resize(src, dsize)

# writng/saving the image/file
cv2.imwrite("Resized_Spideerman.jpg", res_img)

# for showing the image 
print("Showing the result")
src2 = cv2.imread("Resized_Spideerman.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("Resized_Spideerman.jpg", src2)
cv2.waitKey(0)

