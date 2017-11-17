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
        self.speed=[]
        self.total_distance=0
        
def calculate_time(timeS,timeE):
    s1=int(timeS.split(":")[0])
    s2=int(timeS.split(":")[1])
    s3=int(timeS.split(":")[2])
    e1=int(timeE.split(":")[0])
    e2=int(timeE.split(":")[1])
    e3=int(timeE.split(":")[2])
    return (e3-s3+(e2-s2)*60+(e1-s1)*3600)
    
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
with open('28.csv', 'r') as csvfile:
    spamreader=csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in range(0,2000):  #read first 200(4,6,7)
        buffer.append(spamreader.next())
for item in buffer:
    if not item[1].split("|")[4] in check:
        check.append(item[1].split("|")[4])
        list.append(people(item[1].split("|")[6],item[1].split("|")[7],item[1].split("|")[4]))
        list[len(list)-1].route.append([item[1].split("|")[7],item[1].split("|")[6]])
        list[len(list)-1].start_time=item[1].split("|")[0]
        list[len(list)-1].lastx=list[len(list)-1].startx
        list[len(list)-1].lasty=list[len(list)-1].starty
    else:
        #ind=0
    
        for i in list:
            if i.iden==item[1].split("|")[4] and (not i.status=="ended"):
                distance_gap=distance(float(i.lasty),float(item[1].split("|")[7]),float(i.lastx),float(item[1].split("|")[6]))
                cur_speed=distance_gap*1000/calculate_time(pre[1].split("|")[0],item[1].split("|")[0])
                if(cur_speed>=0.5):
                    #if i.status=="nul":
                    #    i.start_time=item[1].split("|")[0]
                    i.end_time=item[1].split("|")[0]
                    if (i.status!="ended"):
                        i.status="started" 
                    i.lastx=item[1].split("|")[6]
                    i.lasty=item[1].split("|")[7]
                    #print item[1].split("|")[0]
                    #print distance_gap
                    #time_diff=calculate_time(pre[1].split("|")[0],item[1].split("|")[0])
                    if (i.status=="started"):
                        i.speed.append(cur_speed)
                    if (i.status=="started"):
                        i.total_distance+=distance_gap
                    i.route.append([item[1].split("|")[7],item[1].split("|")[6]])
                elif i.status=="nul":
                    i.start_time=item[1].split("|")[0]
                    i.startx=item[1].split("|")[6]
                    i.starty=item[1].split("|")[7]
                    i.lastx=item[1].split("|")[6]
                    i.lasty=item[1].split("|")[7]
                elif i.status=="started":
                    i.status="ended"
                    i.end_time=pre[1].split("|")[0]
            #ind+=1
    pre=item
                
startax=[]
startay=[]
lastax=[]
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
        
        print "individual record starts here."
        print item.status
        print item.distance
        print item.route
        print item.start_time
        print item.end_time
        print item.startx
        print item.starty
        print item.lastx
        print item.lasty
        print item.speed
        
        print item.total_distance*1000/calculate_time(item.start_time,item.end_time)
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
