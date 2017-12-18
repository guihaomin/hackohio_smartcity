import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

a=np.load("speeddata.npy")
s=[]
for item in a:
    if(0<float(item[0])<35):
        s.append(float(item[0]))
    if(10.32662<=float(item[0])):
        if ('output' in locals()):
            output=np.vstack([output,item])
            
        else:
            output=np.array(item)
            print output
num_bins = 20
n, bins, patches = plt.hist(s, num_bins,normed=1, facecolor='blue', alpha=0.5)
#plt.show()
print len(output)*1.0/len(a)
#np.save("busdata",output)
    

