import csv
from math import sin, cos, sqrt, atan2, radians
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
class people:
    def __init__(self,startx,starty,iden):
        self.iden=iden
        self.startx=startx
        self.starty=starty
        self.lastx="1"
        self.lasty="1"
        self.status="nul"
        self.distance=0
        self.route=[]
        self.time=[]
        self.start_time=""
        self.end_time=""

def distance(lon1,lon2,lat1,lat2):
    R=6373.0
    lon2=radians(lon2)
    lon1=radians(lon1)
    lat1=radians(lat1)
    lat2=radians(lat2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance
buffer=[]
check=[]
list=[]
with open('16.csv', 'r') as csvfile:
    spamreader=csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in range(0,2000):  #read first 200(4,6,7)
        buffer.append(spamreader.next())
for item in buffer:
    ctime=item[1].split("|")[0]
    if not item[1].split("|")[4] in check:
        check.append(item[1].split("|")[4])
        list.append(people(item[1].split("|")[6],item[1].split("|")[7],item[1].split("|")[4]))

        list[len(list)-1].time.append(ctime)
        list[len(list)-1].route.append([item[1].split("|")[7],item[1].split("|")[6]])
    else:
        for i in list:
            if i.iden==item[1].split("|")[4]:
                loc=0
                while ctime>i.time[loc] and loc<=len(i.time)-1:
                    loc+=1
                    if loc==len(i.time):
                        break
                i.time.insert(loc,ctime)
                i.route.insert(loc,[item[1].split("|")[7],item[1].split("|")[6]])
                break
f=open("newer.txt","w")
f.write("shape_line\n")
for item in list:
    #print item.route
    print item.time
    print item.route
    f.write("\""+str(item.route).replace(" ","").replace("\'","")+"\"\n")
f.close()
"""
lastay=[]
f=open("new.csv","w")
f.write("shape_line\n")
for item in list:
    startax.append(item.startx)
    startay.append(item.starty)
    if item.status=="started" or item.status=="ended":
        item.distance=distance(float(item.starty),float(item.lasty),float(item.startx),float(item.lastx))
    if not (item.status=="nul" or item.distance<0.6):
    #if True:
        f.write("\""+str(item.route).replace(" ","").replace("\'","")+"\"\n")
        #f.write(item.startx+","+item.starty+"\n")
        
                      
        print item.status
        print item.distance
        print item.route
        print item.start_time
        print item.end_time
        print item.startx
        print item.starty
        print item.lastx
        print item.lasty
    if item.lastx=="1":
        lastax.append(item.startx)
        lastay.append(item.starty)
    else: #x is latitude
        lastax.append(item.lastx)
        lastay.append(item.lasty)
plt.plot(startax,startay,'ro',lastax,lastay,'bo')
#plt.plot(lastax,lastay,'ro')
#for i in range(0,len(startax)):
#plt.plot(float(startax[i]),float(startay[i]),float(lastax[i]),float(lastay[i]),#'o')
f.close()

plt.show()
"""
