#****************** DITHERING*************
import numpy as np  
import matplotlib
import matplotlib.pyplot as plt
import pylab
from PIL import Image

im = Image.open("colors.jpg")
#im.show()
M=np.array(im)
           
r=M[:,:,0]/255 #funkcje napisalam w 0..1 a obrazek mam w 0..255
g=M[:,:,1]/255 #wyciagam z obrazka 3 macierze 2 wymiarowe
b=M[:,:,2]/255


def dithering(N):

    for x in range(N.shape[0]):     #przechodze po wszystkich pikselach w wymiarze 2
        for y in range(N.shape[1]):
            if N[x,y] > 0.5: 


                if y+1<=N.shape[1]-1:    #warunek na istnienie sasiada w 7/16, bez prawego brzegu
                    N[x, y+1] = N[x, y+1] + (N[x,y]-1)*7/16 # stara wart + (oldpixel - newpixel)*7/16
                if (x+1 <= N.shape[0]-1) and (y+1<=N.shape[1]-1): # war na istnienie sasiada w 1/16, bez dolnego i prawego  brzegu
                    N[x+1,y+1] = N[x+1,y+1]+ (N[x,y]-1)*1/16
            
                if (x+1 <= N.shape[0]-1): # ...sasiada w 5/16, bez dolnego brzegu
                    N[x+1,y] = N[x+1,y] + (N[x,y]-1)*5/16
                if (x+1 <= N.shape[0]-1) and (y-1 <= N.shape[1]-1 and y-1 >=0):# ...w 3/16, bez lewego brzegu
                    N[x+1,y-1] = N[x+1,y-1]+(N[x,y]-1)*3/16
                N[x,y] = 1
            
            else:
                if y+1<=N.shape[1]-1:
                    N[x, y+1] = N[x, y+1] + (N[x,y])*7/16
                if (x+1 <= N.shape[0]-1) and (y+1<=N.shape[1]-1): 
                    N[x+1,y+1] = N[x+1,y+1]+ (N[x,y])*1/16
            
                if (x+1 <= N.shape[0]-1):
                    N[x+1,y] = N[x+1,y] + (N[x,y])*5/16
                if (x+1 <= N.shape[0]-1) and (y-1 <= N.shape[1]-1 and y-1 >=0):
                    N[x+1,y-1] = N[x+1,y-1]+(N[x,y])*3/16
                N[x,y] = 0
            
    return(N)
R1 =dithering(r)
G1 =dithering(g)
B1 =dithering(b)
#print(G1)
R1G1B1=np.dstack([R1,G1,B1]) # 3 macierze 2 wymiarowe w 1 3wymiarowa
#print(R1G1B1.shape)
newR1G1B1=R1G1B1*255 # musze wrocic do 0..255 bo inaczej w PIL nie dziala
Image.fromarray(newR1G1B1.astype(np.uint8)).show()
result=Image.fromarray(newR1G1B1.astype(np.uint8))
result.save('dithering.bmp')
