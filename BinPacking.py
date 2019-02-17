import csv
import pandas as pd

class Box:
    #this contains the attributes of BOXES
        def __init__(self,
                     ID,
                     name,
                     x,
                     y,
                     z):
            
           self.ID= ID
           self.name= name
           self.x= x
           self.y= y
           self.z= z
           self.vol= self.x * self.y * self.z

        def tostring(self): 
                print("Box--- ID:",self.ID,"name",self.name,"vol:",self.vol)
                
class BoxFinal:
    #this contains the attributes of BOXES
    def __init__(self,
                 ID,
                 name,
                 box,
                 level,
                 coor_x,
                 coor_y,
                 coor_z,
                 Rot):
        
        self.ID= ID
        self.name = name
        self.box = box
        self.level = level
        self.coor_x = coor_x
        self.coor_y = coor_y
        self.coor_z = coor_z
        self.Rot = Rot
    

def compare(b1, b2):
        return int(b1.z - b2.z)

def compare_ht(b1, b2):
        return int(b1.vol - b2.vol)


def compare_ID(b1, b2):
        return (b1.ID - b2.ID)

class Level:
     def __init__(self, l, ht):
        self.l = l
        self.ht = ht
        
     def tostring():
             print("sheet info",self.l,"height",self.ht)

class Container:
    #this conatins the attributes of CONTAINERS

    def __init__(self,
                 ID,
                 name,
                 x,
                 z,
                 y):

        self.ID = ID
        self.name = name

        self.x = x
        self.y = y
        self.z = z

        self.z_orig = z

        self.vol = x*y*z
        
        self.xt = x
        self.yt = y
        self.zt = z
        
        self.level = 0

        self.flag_rev= False
        self.first_flag = True
        self.flag_level = False

        self.cx= 0
        self.cy= 0
        self.cz= 0
        self.levels = []

class BinPacking:

    def __init__(self):
       self.boxes = []
       self.cont = 0
       self.boxesfinal = []
       
       self.n=0

       self.tp1 = 0
       self.tp2 = 0
       self.cff = 0
       self.cfk = 0
       self.tmp = 0
       self.c = 0
       self.flag_tmp = 0
       self.Rot = False

       self.BOX_ID_IDX = 0
       self.BOX_NAME_IDX = 1
       self.BOX_X_IDX = 2
       self.BOX_Y_IDX = 3
       self.BOX_Z_IDX = 4

       self.CONT_ID_IDX = 0
       self.CONT_NAME_IDX = 1
       self.CONT_X_IDX = 2
       self.CONT_Y_IDX = 3
       self.CONT_Z_IDX = 4

    def read_boxes_file(self):
        try:
           with open('../Data/Boxes.csv','rt',encoding='UTF8') as f:
              r = csv.reader(f)
              next(r)
              for ro in r:
                   self.boxes.append(Box(ro[self.BOX_ID_IDX],
                                         ro[self.BOX_NAME_IDX],
                                         int(float(ro[self.BOX_X_IDX])),
                                         int(float(ro[self.BOX_Y_IDX])),
                                         int(float(ro[self.BOX_Z_IDX]))))
              for h in self.boxes:
                  h.tostring()
        except Exception as e:
            print(e)
            
    def read_conts_file(self):
        try:
           with open('../Data/Conts.csv','rt',encoding='UTF8') as f:
              r = csv.reader(f)
              next(r)
              for ro in r:
                 self.cont = Container(ro[self.CONT_ID_IDX],
                                       ro[self.CONT_NAME_IDX],
                                       int(ro[self.CONT_X_IDX]),
                                       int(ro[self.CONT_Y_IDX]),
                                       int(ro[self.CONT_Z_IDX]))
              
        except Exception as e:
            print(e)              
                    
    def iterr(self,box):
                     
                    self.flag_tmp = False             #flag_tmp is used to check whether box is added or not if not added it will print the box 
                    self.tp1 = self.cont.xt           #tp1 is storing the remaining length of container x side
                    self.tp2 = self.cont.yt           #tp2 is storing the remaining length of container y side
                    
                    if self.cont.flag_rev == False:     #cont.flag_rev is a flag variable to initially assign cont.zt
                        self.cont.zt = box.z            
                        self.cont.flag_rev = True       #as it is initially assigned it is changed to true
                    

                    if self.cont.vol>=box.vol:                                #checking if box volume constraint is matched
                        self.cff = 0                                                 #cff is a counter variable to store number of combinations
                    
                        while(self.cff<=9):
                            if(self.cont.zt >=box.z or
                               self.cont.z >=box.z):                                      #checking whether the container height is fitting the box or not
                                self.cfk = 0                                              #cfk is a counter variable to store number of combinations
                                
                                while(self.cfk<=6):
                                    if(self.cont.xt>=box.x and
                                       self.cont.yt>=box.y):                              #if the box fits the remaining space then
                                       
                                        self.cont.vol -= box.vol                          #decrementing cont volume
                                                    
                                        self.tmp = self.cont.zt                               #tmp is a temporary variable to store previous max height of that level
                                        self.cont.zt = max(self.cont.zt, box.z)                #changing cont.zt

                                        if self.cont.zt != self.tmp:                            #if it is not equal 
                                            self.cont.z = self.cont.z - self.cont.zt + self.tmp         #chaning the cont.z --visualize IT
                                        
                                        if self.cont.first_flag == True:                    #for the first time the container is choosen
                                            self.cont.z -= self.cont.zt
                                            self.cont.first_flag = False                    #toggling the cont.first_flag
                                            self.cont.level += 1                            #for initial level leveling up
                                        #Making new reference and Adding the box into the BoxFinal reference
                                        tp = BoxFinal(self.cont.ID,
                                                      self.cont.name,
                                                      box,
                                                      self.cont.level,
                                                      self.cont.x-self.cont.xt,
                                                      self.cont.y-self.cont.yt,
                                                      self.cont.z-self.cont.zt,
                                                      self.Rot)
                                        
                                        self.boxesfinal.append(tp)
                                        
                                        self.c -= 1
                                        self.cff += 1
                                        self.cfk += 1

                                        self.flag_tmp = True

                                        #two temporary variables changing to find the maximum sized rectangle --visualize IT
                                        self.tp1 -= box.x
                                        self.tp2 -= box.y

                                        if(self.tp1 > self.tp2):
                                            self.cont.xt = self.tp1
                                        
                                        elif(self.tp1<self.tp2):
                                            self.cont.yt = self.tp2
                                        
                                        #as box is added break the OUTER loop and add another box
                                        return
                                    
                                    #if box is not added due to reduced space but there is scope of level available --VISUALIZE IT
                                    elif(self.cont.z>=box.z and
                                            (self.cont.x>=box.x and self.cont.y>=box.y) and
                                            (self.cont.xt<box.x or self.cont.yt<box.y)):
                                            
                                        tlevel = Level(self.cont.level,self.cont.z_orig - self.cont.z)               #creating reference of level
                                        self.cont.levels.append(tlevel)                                         #adding the old level height

                                        self.cont.level += 1                                                    #leveling up
                                        self.cont.xt = self.cont.x                                                #reseting the contatiner xt and yt
                                        self.cont.yt = self.cont.y

                                        self.tp1 = self.cont.x                                                    #leveling up
                                        self.tp2 = self.cont.y                                                    #so resetting the container temp variables

                                        self.cont.zt = box.z                                                 #changing the container zt
                                        self.cont.z -= self.cont.zt
                
                                        self.cont.flag_level = True                                          #as it is leveling up so flag is changed

                                        self.cff += 1
                                        self.cfk += 1
                                    
                                    else:
                                        #else twisting the container
                                        t5 = box.x
                                        box.x = box.y
                                        box.y = t5
                                        self.Rot='z'

                                        self.cff += 1 
                                        self.cfk += 1 
                   
                            elif (self.cont.z>=box.z) and (box.y<box.x):
                                #vertically twisting the conatiner having least height --VISUALIZE IT
                                self.cont.zt = max(self.cont.zt,box.y)

                                th = box.z
                                box.z = box.y
                                box.y = th
                                self.Rot='x'

                                self.cff += 1
                            
                            elif (self.cont.z>=box.z) and (box.x<box.y):
                                #vertically twisting the conatiner having least height --VISUALIZE IT
                                self.cont.zt = max(self.cont.zt,box.x)

                                th = box.z
                                box.z = box.x
                                box.x = th  
                                self.Rot='y'
                                
                                self.cff += 1
                            
                            else:
                                #if none of the cases are true
                                #incrementing the combinations to make while loop to end
                                self.cff += 1
                    else:
                          print("box bigger than container")      

    def least_no_boxes(self):
            print("###---LEAST NUMBER OF BOXES---###")

            self.c = len(self.boxes)   #c stores the number of boxes

            print("List of boxes may or maynot fit:-")
            #for each box trying to fit in the smallest container first
            #if it does not fit try the next smallest container
            for box in self.boxes:                
                self.iterr(box)

            print("The boxes and containers are:-")
            tp_prev_id = 1
            d = {'Mesh ID': [], 'Mesh name': [],'x_coords': [],'y_coords': [],'z_coords': [],'Rot':[]}
            df = pd.DataFrame(data=d)
            for tp in self.boxesfinal:
                if tp_prev_id != tp.ID:
                    print("")
                print("Mesh ID:",tp.box.ID,"Mesh Name:",tp.box.name," x_coords:",tp.coor_x," y_coords:",tp.coor_y,"z_coords:",tp.coor_z,"Rot:",tp.Rot)
                df = df.append({'Mesh ID': tp.box.ID, 'Mesh name': '%s'%tp.box.name,'x_coords': tp.coor_x,'y_coords': tp.coor_y,'z_coords': tp.coor_z,'Rot':tp.Rot}, ignore_index=True)
                tp_prev_id = tp.ID
           
            df = df[['Mesh ID', 'Mesh name','x_coords','y_coords','z_coords','Rot']]      
            print("Total number of boxes=",len(self.boxes))
            print("Number of boxes left=",self.c)
            df.to_csv("../Data/mesh.csv", index=False)

"""                  _    
                    | |
                    | |                     
                ____| |____
               |___________|

               x1 y1 z1
               x2 y2 z2 po_x po_y po_z
               while ID:
                   if z:
                      if y&x:
                         tmpdims = realdims - box dim
                         tmpbox = box
                         IDcontinuous = true
                      else:
                         remove tmpbox,tmpdims 
                         treat whole thing as one box  
                         IDcontinuous = false
                   else:
                      remove tmpbox,tmpdims 
                      treat the whole thing as one box(add the identical IDs dims together, box them , then pass them to be processed and skip till the next ID)                         
                      IDcontinuous = false
              if IDcontinuous == False:
                   treat whole thing as one big box or maybe rotate it                                   
"""
