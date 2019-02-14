import stl
import numpy
from stl import mesh
import pandas as pd
import csv

x_Tolerance=1.5
y_Tolerance=1.5
z_Tolerance=1.5
z_axis=False

def find_mins_maxs(obj):
        return numpy.amin(obj.v0[0]),numpy.amax(obj.v0[0]),numpy.amin(obj.v1[0]),numpy.amax(obj.v1[0]),numpy.amin(obj.v2[0]),numpy.amax(obj.v2[0])

main_body = mesh.Mesh.from_file('../Mesh/1.stl')
minx1, maxx1, miny1, maxy1, minz1, maxz1 = find_mins_maxs(main_body)
main_body.translate([-minx1,-miny1,-minz1])

mesH = []
x=[]
y=[]
z=[]

with open('../Data/mesh.csv','rt',encoding='UTF8') as f:
              r = csv.reader(f)
              next(r)
              for ro in r:
                   x.append(int(float(ro[2])))
                   y.append(int(float(ro[3])))
                   z.append(int(float(ro[4])))

if z_axis == False:
     z=[0]*len(z)

for i in range(2,len(x)):
   meshh = mesh.Mesh.from_file('../Mesh/%d.stl'%i)
   minx2, maxx2, miny2, maxy2, minz2, maxz2 = find_mins_maxs(meshh)
   if z_axis is False:
       maxz2=0
   meshh.translate([-maxx2,-maxy2,-maxz2])
   meshh.translate([x[i-1]/x_Tolerance,y[i-1]/y_Tolerance,z[i-1]/z_Tolerance])
   mesH.append(meshh)
combined = mesh.Mesh(numpy.concatenate([main_body.data]+[meshee.data for meshee in mesH]))
combined.save('../Finale/combined.stl')
#v3,c3,i3 = meshhh.get_mass_properties()
