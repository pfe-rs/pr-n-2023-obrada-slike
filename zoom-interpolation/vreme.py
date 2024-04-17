import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time
"""
Ovaj fajl sluzi za mernje perioda izvršavanja
interpolacija.
"""

img = cv.imread('zaba.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
zoom_parametar = 2.0


def zoomSlike(scale,slika):
    #Napravljene nove dimenzije slike
    rows, cols, kanal = slika.shape
    new_rows = int(rows * scale)
    new_cols = int(cols * scale)

    rezultat = np.zeros((new_rows, new_cols, kanal), dtype=np.uint8)
    
    for i in range(rows):
        for j in range(cols):
            rezultat[int(i * scale), int(j * scale)] = slika[i, j]
    
    konacni_rezultat= np.zeros((rows,cols,kanal),dtype=np.uint8)

    for i in range(rows):
        for j in range(cols):
            konacni_rezultat[i,j]=rezultat[i,j]

    return konacni_rezultat



def interPolacijaNajblizegKomsije(zoomed,slika,scale):
    rows=slika.shape[0]
    cols=slika.shape[1]
    rezultat=zoomed.copy().astype("int")
    for i in range(rows):
        for j in range(cols):
            if np.any(rezultat[i,j]==0):
                rezultat[i,j] = slika[int(i/scale), int(j/scale)]
    
    return rezultat

def bilinearnaInterpolacija(zoomed):
    rows=zoomed.shape[0]
    cols=zoomed.shape[1]
    bilinear=zoomed.copy().astype("int")
    #horiznotalni
    for i in range(0,rows-1,2):
        for j in range(1,cols-1,2):
            bilinear[i,j]=(bilinear[i,j-1]+bilinear[i,j+1])//2
    #vertikalini
    for i in range(1,rows-1,2):
        for j in range(0,cols-1,2):
            bilinear[i,j]=(bilinear[i-1,j]+bilinear[i+1,j])//2
    #srednji
    for i in range(1,rows-1,2):
        for j in range(1,cols-1,2):
            bilinear[i,j]=(bilinear[i-1,j]+bilinear[i+1,j]+bilinear[i,j-1]+bilinear[i,j+1])//4

    konacna_bilinear=np.zeros((rows-1,cols-1,3),dtype='int')
    for i in range(rows-1):
        for j in range(cols-1):
            konacna_bilinear[i,j]=bilinear[i,j]

    return konacna_bilinear

startZaZoom=time.time()
zumirana=zoomSlike(zoom_parametar,img)
endZaZoom=time.time()
#vreme izvrsavanja zoom funkcije
vremeZaZoom=endZaZoom-startZaZoom

startZaNajb=time.time()
najblizi=interPolacijaNajblizegKomsije(zumirana,img,zoom_parametar)
endZaNajb=time.time()
#vreme izvrsavanje interpolacije najbli. suseda
vremeZaNajb=endZaNajb-startZaNajb

startZaBil=time.time()
bilinearna = bilinearnaInterpolacija(zumirana)
endZaBil=time.time()
#vreme izvrsavanja bilinearne interpolacije
vremeZaBil=endZaBil-startZaBil

print(vremeZaZoom)
print(vremeZaBil)
print(vremeZaNajb)


x = [vremeZaBil,vremeZaNajb,0.63,1.32]

metode = ['Najbliži Sused(zaba.jpg)', 'Bilinearna(zaba.jpg)','Najbliži sused(suncokret.jpg)','Bilinearna(suncokret.jpg)']

plt.bar(metode, x, color=['red', 'blue','red','blue'])
plt.ylabel('Vreme (s)')
plt.xlabel('Metode Interpolacije')
plt.title('Vreme Izvršavanja Bilinearne i Najbližeg Suseda Interpolacije')
plt.show()