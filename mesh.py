import stl
import numpy
from stl import mesh
import pandas as pd
import csv
import subprocess
import math

mesH = []
ID= []
x= []
y= []
z= []
Ro= []

#Read user defined parameters
with open("../Bins/parameters.txt") as f:
        params = f.readlines()
        
x_Tolerance= float(params[2][12:])
y_Tolerance= float(params[3][12:])
z_Tolerance= float(params[3][12:])
z_axis= int(params[5][7:])

#find min and max dimensions for mesh
def find_mins_maxs(obj):
        return numpy.amin(obj.v0[0]),numpy.amax(obj.v0[0]),numpy.amin(obj.v1[0]),numpy.amax(obj.v1[0]),numpy.amin(obj.v2[0]),numpy.amax(obj.v2[0])

#read data about position and orientation of meshes and save to arrays  
with open('../Data/mesh.csv','rt',encoding='UTF8') as f:
              r = csv.reader(f)
              next(r)
              for ro in r:
                   ID.append(int(float(ro[0])))
                   x.append(int(float(ro[2])))
                   y.append(int(float(ro[3])))
                   z.append(int(float(ro[4])))
                   Ro.append(str(ro[5]))

#make first mesh the origin mesh so other meshes are placed relative to it
#we translate the mesh to its origin because stl has no way of describing coordinates in space
main_body = mesh.Mesh.from_file('../Mesh/1.stl')
minx1, maxx1, miny1, maxy1, minz1, maxz1 = find_mins_maxs(main_body)
main_body.translate([-minx1,-miny1,-minz1])

#z-axis was throwing me off in the visualization so i had to disable it at first
if z_axis == 0:
     z=[0]*len(z)

#iterate over meshes , rotate them, translate them to their own origin then translate them relative to the previous point
#such that each point has a origin the previous point
for i in range(2,len(x)):
   meshh = mesh.Mesh.from_file('../Mesh/%d.stl'%ID[i])
   #minx2, maxx2, miny2, maxy2, minz2, maxz2 = find_mins_maxs(meshh)   
   if Ro[i] != '0.0':
           if Ro[i] == 'z':
                   meshh.rotate([0.0,0.0,0.5],math.radians(90))
           elif Ro[i] == 'y':
                   meshh.rotate([0.0,0.5,0.0],math.radians(90))
           elif Ro[i] == 'x':
                   meshh.rotate([0.5,0.0,0.0],math.radians(90))
                  
   minx2, maxx2, miny2, maxy2, minz2, maxz2 = find_mins_maxs(meshh)
   if z_axis == 0:
       maxz2=0
   meshh.translate([-maxx2,-maxy2,-maxz2])
   meshh.translate([x[i-1]/x_Tolerance,
                    y[i-1]/y_Tolerance,
                    z[i-1]/z_Tolerance])
   mesH.append(meshh)
combined = mesh.Mesh(numpy.concatenate([main_body.data]+[meshee.data for meshee in mesH]))

#instead of replacing the file each time we do this, i create a new file alongside a text file containing the chosen parameters
#for the purpose of helping revision
task = subprocess.Popen("ls -1v ../Finale",shell=True,stdout=subprocess.PIPE)
last_mesh = task.stdout.read()
if len(last_mesh) == 0:
        with open("../Finale/combined_001.txt", 'w+') as f:
                  f.write("x_tolerance ="+ str(x_Tolerance)+
                          "\ny_tolerance ="+str(y_Tolerance)+
                          "\nz_tolerance ="+str(z_Tolerance))
                  
        combined.save('../Finale/combined_001.stl')        
else:
    last_mesh = int(last_mesh[-8:-5])
    with open("../Finale/combined_%03d.txt"%(last_mesh+1), 'w+') as f:
                  f.write("x_tolerance ="+ str(x_Tolerance)+
                          "\ny_tolerance ="+str(y_Tolerance)+
                          "\nz_tolerance ="+str(z_Tolerance))
    combined.save('../Finale/combined_%03d.stl'%(last_mesh+1))
#v3,c3,i3 = meshhh.get_mass_properties()
