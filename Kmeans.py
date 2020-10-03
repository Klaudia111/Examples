#to run: python3 KMeans.py
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


Data = {'x': [1,2,3,4,5,6,7],
        'y': [2,1,5,7,10,11,14]}
df = DataFrame(Data,columns=['x','y'])
  
kmeans = KMeans(n_clusters=3).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)
km=KMeans(n_clusters=3)
predicted = km.fit_predict(df)
print(predicted)
df['cluster']=predicted
#plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=100, alpha=2) #all points, s-size, alpha-transparency
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=100, alpha=0.3) #middle of clusters
df1 = df[df.cluster==0]
plt.scatter(df1['x'], df1['y'], color='green', s=80, alpha=1)
df2 = df[df.cluster==1]
plt.scatter(df2['x'], df2['y'], color='blue', s=80, alpha=1)
df3 = df[df.cluster==2]
plt.scatter(df3['x'], df3['y'], color='yellow', s=80, alpha=1)

plt.axvspan(0,10,facecolor='orange', alpha=0.2) 
plt.title('K-means clusters')
plt.xlabel("x")
plt.ylabel("y")
plt.show()

