import cv2
image=cv2.imread('eng.png') #must be save in same path of the project

B,G,R=cv2.split(image) #function splits the imageinti each color index
cv2.imshow("Red",R) #the basic colors
cv2.imshow("Green",G)#"color name" is the name that will present in the image window
cv2.imshow("Blue",B)
#merging the individual color components
merged=cv2.merge([B,G,R])
cv2.imshow("merged",merged)
#amplifying the blue color
merged=cv2.merge([B+40,G,R])
cv2.imshow("merged with blue amplify",merged)
#print the image window
print(B.shape)
print(R.shape)
print(G.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
