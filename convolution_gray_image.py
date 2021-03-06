"""
This file takes a image name and performs a convulation operation 
output : Display image and write image to disk 
Filter: 2 filter can be choosen horizontal of vertical of size -3  
"""
import cv2
import numpy as np 


img = cv2.imread('face.jpeg')

#Change image to Grey
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



#suppose we have filter of size 3 
#Vertical Filter
filt = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
#Horizontal Filter
filt = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])


#Lets check shape of Image 
H_img,W_img = img.shape
print("Shape of Image H x W:",H_img,W_img)


#Lets check shape of filter 
H_filt,W_filt = filt.shape
print("Shape of the Filter H x W:",H_filt,W_filt)



new = [] # append convulated output ie: one number to this array later reshape 


for i in range(0,(W_img + 1) - W_filt):
	# i - for loop will move vertically
	for j in range(0,(H_img + 1)- H_filt):
		# j - Loop will move Horizontally 

		#Selecting a window 
		conv = img[0 + j:H_filt + j , 0+i:W_filt+i]
		#Applying filter _ Multiplying selected window with filter 
		final = conv * filt
		#Applying filter _ Adding output of multiply 
		final = final.sum()
		#Saving output to new as list 
		new.append(final)

print("Length of the new List:", len(new))
print("Reshape list to create new array/Image of H x W:",(H_img - H_filt) + 1 ,(W_img - W_filt) + 1 )

newImage = np.array(new)
# Formula - n-f + 1 * n-f + 1 
newImage = newImage.reshape( (H_img - H_filt) + 1 ,(W_img - W_filt) + 1)

print("Printing new created image")
print(newImage)


cv2.imshow('image',newImage)
cv2.imwrite('conv.jpg',newImage)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
