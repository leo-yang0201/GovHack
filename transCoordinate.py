# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pyproj

x = []   #lontitude  经度
y = []   #latitude   纬度
m = []


path = "C:/Users/thinkpad/Desktop/"
fin = open(path+"b.txt", "rt",encoding= 'utf-8') 
fout = open(path+ "coordinate.txt", "wt",encoding= 'utf-8')

i = 0   
for line in fin:
    print(line)
    m = line.split('\t')
    newline = []
    s = '' 
    newline.append(m[0]) 
    k = len(m) 
    print(k)
    p = 1 
    while p < k-1:
        save = [1,2]
        save = m[p].split(',')
        lat = save[0] #1
        lon = save[1]  #2
        print(save[0],save[1])
        print(p)
        proj_GDA94 = pyproj.Proj(init="epsg:3111")
        proj_wgs84 = pyproj.Proj(init="epsg:4326")
        a, b = pyproj.transform(proj_GDA94, proj_wgs84, lon, lat)
        print(a,b)
        newline.append(a) 
        newline.append(b)
        p += 1  
    
    for item in newline:
        s = s +' '+ str(item)
    print(s)
    fout.write(s)
    #s = newline[0]+''+newline    
    #fout.write('%-10s%-11s%-11s\n' %(name[i],y[i],x[i]))          
    #'%-10s%-11s%-11s' %(name[i],y[i],x[i]))  #先纬度后经度
    i += 1


fin.close()
fout.close()

