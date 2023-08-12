import cv2
import numpy as np
from skimage import io
import matplotlib
import matplotlib.pyplot as plt

#pomocu ove funkcije uklanjamo senku
def removing_shadow(img):
   
    # pocetna slika se konvertuje u gray scale sliku
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # primenjujemo filter GassianBlur kako bismo smanjili sum na slici
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # primenjujemo adaptivni treshold, konverujemo sliku u binarizovanu sliku
    thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

    # definisemo kernel za morfoloske operacije
    kernel = np.ones((1,1),np.uint8)

    # primenjujemo morfolosku operaciju closing 
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations = 2)

    # primenjujemo morfolosku operaciju dilate 
    dilated=cv2.dilate(closing, kernel, iterations=1)


    # primenjujemo morfolosku operaciju eroziju
    reconstraction=cv2.erode(dilated, kernel, iterations=1)


    # primenjujemo funkciju bitwise_not kako bismo bele piksele prebacili u crne i crne piksele u bele
    final_img=cv2.bitwise_not(reconstraction)


    #vracamo finalnu sliku
    return final_img


#pomocu ove funkcije izostravamo sliku
def sharpen_image(img):

    # primenjujemo filter GassianBlur kako bismo smanjili sum na slici
    blur = cv2.GaussianBlur(img, (5,5), 0)

    # kernel=np.array([[0,-1,0],
    #                  [-1,5,-1],
    #                  [0,-1,0]])

    # kernel=np.array([[-1,-1,-1,-1,-1],
    #                 [-1,2,2,2,-1],
    #                 [-1,2,2,2,-1],
    #                 [-1,2,2,2,-1],
    #                 [-1,-1,-1,-1,-1]])/8.0

    # #Laplacian kernel
    kernel=np.array([[0,-1,0],
             [-1,4,-1],
             [0,-1,0]])
    
    #primenjujemo filter2D kako bismo izostrili sliku
    img_sharp=cv2.filter2D(blur, -1, kernel)

    #vracamo izostrenu sliku
    return img_sharp


#pomocu ove funkcije podebljavamo slova
def thicken_text(img):
    
    #definisemo kernel za diletaciju
    kernel = np.ones((2,2),np.uint8)

    #primenjujemo diletaciju nad slikom
    new_img=cv2.dilate(img, kernel, iterations=1)

    #vracamo sliku sa podebljanim slovima
    return new_img

#ucitavamo sliku
img=cv2.imread("C:\slike\Tekst_1.png")

#nova slika koju dobijamo primenom funkcije removing_shadow
new_img=removing_shadow(img)

#nova slika koju dobijamo primenom funkcije sharpen_image
img_sharp=sharpen_image(new_img)

#nova slika koju dobijamo primenom funkcije thicken_text
img_dilated=thicken_text(img_sharp)

#krajnja slika 
img_final=cv2.bitwise_not(img_dilated)

fig=plt.figure(figsize=(10,7))

#prikazujemo pocetnu sliku
fig.add_subplot(2,3,1)
plt.imshow(img,cmap='gray')
# #prikazujemo sliku bez senke
fig.add_subplot(2,3,2)
plt.imshow(new_img,cmap='gray')
# #prikazujemo izostrenu sliku
fig.add_subplot(2,3,3)
plt.imshow(img_sharp,cmap='gray')
# #prikazujemo sliku sa podebljanim slovima
fig.add_subplot(2,3,4)
plt.imshow(img_dilated,cmap='gray')
# #prikazujemo kranju sliku
fig.add_subplot(2,3,5)
plt.imshow(img_final,cmap='gray')

plt.show()
