import BinPacking as bp
import stl
import numpy
from stl import mesh
import pandas as pd
import csv	

Mesh_No = 12

def find_mins_maxs(obj):
        return numpy.amin(obj.v0[0]),numpy.amax(obj.v0[0]),numpy.amin(obj.v1[0]),numpy.amax(obj.v1[0]),numpy.amin(obj.v2[0]),numpy.amax(obj.v2[0])

d = {'id': [], 'Name': [],'Width(x)': [],'Height(y)': [],'Length(z)': []}
df = pd.DataFrame(data=d)
for i in range(1, Mesh_No):
    body = mesh.Mesh.from_file('../Mesh/%d.stl'%i)
    minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(body)
    df = df.append({'id': '%d'%i, 'Name': '%d.stl'%i,'Width(x)': maxx-minx,'Height(y)': maxy-miny,'Length(z)': maxz-minz}, ignore_index=True)
df = df[['id','Name','Width(x)','Height(y)','Length(z)']]
df.to_csv("../Data/Boxes.csv", index=False)
