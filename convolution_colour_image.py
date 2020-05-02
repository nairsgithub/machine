"""
This file takes a image name and performs a convulation operation on a Colour Image 
BGR image is read by opencv and all three channels are seperated / Convolution operation is done and combined again 
output : Display image and write image to disk 
Filter: 2 filter can be choosen horizontal of vertical of size -3  
"""
import cv2
import numpy as np 



def convolution(img,Filter="Vertical"):
	"""
	#this convolution function is detailed discussed in : https://github.com/nairsgithub/machine/blob/master/convolution_gray_image.py
	#we have turned that same file as a function to apply convolution here
	#input will be an image and Filter "Vertical" / "Horizontal" - feel free to change this in code

	"""
	#suppose we have filter of size 3 
	#Vertical Filter
	if Filter == "Vertical":
		filt = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
	#Horizontal Filter
	if Filter == "Horizontal":
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
	#return convoluted image 
	return newImage





#The main function for BGR startes here 

#Reding image - opencv reads image as BGR and in numpy datatype 
img = cv2.imread('face.jpeg')

print("Imag is read as :",type(img))


#Create images with single channels 
#Select from all Rows and columns and 1 Item from 3rd Dimension 
"""
img = [   [  [21,22,23],[25,26,27]        ],
		  [  [11,12,13],[15,16,17]  ] 	

for Blue select only : 21,25,11,15
"""
Blue = img[:,:,0] 
Green = img[:,:,1]
Red = img[:,:,2]


# Apply convolution function to each of the channel 
Blue = convolution(Blue,Filter="Horizontal")

Green = convolution(Green,Filter="Horizontal")

Red = convolution(Red,Filter="Horizontal")


#combine each of the channel 
img = np.dstack((Blue,Green,Red))


#appending All three image together to show in one window 

allFilterImages = np.concatenate((Blue,Green,Red),axis=1)





# Write output 
cv2.imshow('image',allFilterImages)
cv2.imwrite('colourConvFinalimage.jpg',img)
cv2.imwrite('colourConvFilterimageBGR.jpg',allFilterImages)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()




