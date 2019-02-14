import BinPacking as bp
import stl
import numpy
from stl import mesh
import pandas as pd
import csv	

h = bp.BinPacking()
h.read_boxes_file()
h.read_conts_file()
h.least_no_boxes()

