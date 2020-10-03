import numpy as np  
import matplotlib
import matplotlib.pyplot as plt
import pylab
from pandas import DataFrame
from sklearn.cluster import KMeans

from PIL import Image
im = Image.open("colors.jpg")
#im.show()
M=np.array(im)

k=16
           
R=M[:,:,0].flatten() #wyciagam czerwien i robie plaska liste
G=M[:,:,1].flatten()
B=M[:,:,2].flatten()
#print(R)

Data = {'r': R,
        'g': G,
        'b': B}
df = DataFrame(Data,columns=['r','g', 'b'])

km=KMeans(n_clusters=k)
predicted = km.fit_predict(df)
#print(predicted) #[6 6 1 ... 2 2 2]


centroids = km.cluster_centers_
#print(centroids)  #[197.32430399  10.72126912   4.02673689], ... x16

newM=np.zeros((len(predicted),3)) #tworze nowa liste, dlugosci predicted, [[0,0,0],[0,0,0]..] i do niej wpisze wyszukane przez algorytm kmeans srodki. Srodki te maja 3 wspolrzedne

for i in range(len(predicted)): #i=0,1,..8
    newM[i] = centroids[predicted[i]]  #tam gdzie na liscie predicted byly 0, to maja byc pierwsze(zerowe) srodki, i tak powstaje newM= [srodek0, sr1, sr0...] 

    #for j in range(k):
     #   if predicted[i] == j:
      #      newM[i] = centroids[j]
#print(newM)
newMM=newM.reshape(M.shape[0],M.shape[1],3) #wracam do oryginalnych wymiarow inputowego obrazka
#plt.imshow((newMM).astype(np.uint8))
#plt.show()
#Image.fromarray(newMM.astype(np.uint8)).show()
result1=Image.fromarray(newMM.astype(np.uint8))
result1.save('kmeans.bmp')
