import cv2
import numpy as np
# read image
src = cv2.imread('images/cameraman.tif', cv2.IMREAD_UNCHANGED)
height, width = src.shape[:2]

kernel = np.ones((5,5),np.float32)/25
dst1 = cv2.filter2D(src,-1,kernel)
edges = cv2.Canny(src,100,200)
biltFilt = cv2.bilateralFilter(src, 15, 75, 75)

final = np.zeros((height, width,1),dtype=np.uint8)
final = biltFilt+edges

#final = np.zeros((height, width,3),dtype=np.uint8)
#final[:,:,0]=biltFilt[:,:,0]+edges
#final[:,:,1]=biltFilt[:,:,1]+edges
#final[:,:,2]=biltFilt[:,:,2]+edges

# display input and output image

#cv2.imshow("src",src)
#cv2.imshow("Smoothing And Canny Edge",np.hstack((src, dst1,edges,biltFilt)))
cv2.imshow("src",src)
#cv2.imshow("blur",dst1)
#cv2.imshow("edges",edges)
cv2.imshow("biltFilt",biltFilt)
cv2.imshow("final",final)

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
