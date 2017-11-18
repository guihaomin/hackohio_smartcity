import numpy as np
from sklearn.cluster import KMeans

a=np.load("speeddata.npy")
y_pred = KMeans(n_clusters=3, random_state=170).fit_predict(a)
import matplotlib.pyplot as plt
X=[]
Y=[]
Xd=[]
Yd=[]
for item in a:
    X.append(item[1])
    Y.append(item[2])
    Xd.append(item[3])
    Yd.append(item[4])
plt.scatter(X, Y, c=y_pred)
plt.show()
plt.clf()
plt.scatter(Xd, Yd, c=y_pred)
plt.show()
