import BinPacking as bp
import stl
import numpy
from stl import mesh
import pandas as pd
import csv
import subprocess

#Read user defined parameters
with open("../Bins/parameters.txt") as f:
        Randomize= int(f.readline()[10:])
        Rotate = int(f.readline()[7:])
        
#induce a bash task , count number of meshes inside
task = subprocess.Popen("ls -1 ../Mesh| wc -l",shell=True,stdout=subprocess.PIPE)
Mesh_No = task.stdout.read()
Mesh_No = int(Mesh_No)+1

#find min and max dimensions in mesh
def find_mins_maxs(obj):
        return numpy.amin(obj.v0[0]),numpy.amax(obj.v0[0]),numpy.amin(obj.v1[0]),numpy.amax(obj.v1[0]),numpy.amin(obj.v2[0]),numpy.amax(obj.v2[0])

#initialize dataframe
d = {'id': [], 'Name': [],'Width(x)': [],'Height(y)': [],'Length(z)': []}
df = pd.DataFrame(data=d)

#iterate over meshes
for i in range(1, Mesh_No):
    body = mesh.Mesh.from_file('../Mesh/%d.stl'%i)
    minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(body)
    df = df.append({'id': '%d'%i, 'Name': '%d.stl'%i,'Width(x)': maxx-minx,'Height(y)': maxy-miny,'Length(z)': maxz-minz}, ignore_index=True)

#order columns    
df = df[['id','Name','Width(x)','Height(y)','Length(z)']]
#randomize
if Randomize == 1:
        df = df.sample(frac=1).reset_index(drop=True)
#save
df.to_csv("../Data/Boxes.csv", index=False)
