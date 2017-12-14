import numpy as np
from sklearn.cluster import KMeans

a=np.load("speeddata.npy")
y_pred = KMeans(n_clusters=5, random_state=170).fit_predict(a)
import matplotlib.pyplot as plt
X=[]
Y=[]
Xd=[]
Yd=[]
for item in a:
    X.append(item[2])
    Y.append(item[1])
    Xd.append(item[4])
    Yd.append(item[3])
color=[]
hypoX=[]
hypoY=[]
for i in range(0,len(y_pred)):
    if(y_pred[i]==0):
        color.append("red")
        hypoX.append(a[i][2])
        hypoY.append(a[i][1])
    elif(y_pred[i]==1):
        color.append("white")
     #  hypoX.append(a[i][2])
     #  hypoY.append(a[i][1])
    elif(y_pred[i]==2):
        color.append("white")
    elif(y_pred[i]==3):
        color.append("white")
      # hypoX.append(a[i][2]) #copy this 2 lines aroung to see different cluster
      # hypoY.append(a[i][1])
    elif(y_pred[i]==4):
        color.append("white")
#plt.scatter(X, Y, c=color)
print len(a)
plt.scatter(hypoX, hypoY)
plt.show()
plt.clf()
#plt.scatter(Xd, Yd, c=y_pred)
plt.show()
