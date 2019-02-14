So i have seperated this into different folders so i can work , upload to the website and u just pull everyday to get the latest version.
# First step
make a folder with any name u want, go inside,

make 3 files named `Data` `Finale` `Mesh`,

then do `git clone https://github.com/ahmedmdl/Executable`.

u should get the *Executable* folder now.

# Operation
everyday u wake up and want to try , do `git pull`,and u will get my latest updates.

## Operation instructions
`python3 Construct.py`

`python3 Pack.py`

`python3 mesh.py`

then check the finale folder, u can use blender to open it 

# Concept
## Inside the Mesh folder:
  put as much meshes as u can starting with their names starting from *1.stl* just incrementing the number.
  
  u can put high res meshes as well and i encourage that.


## Inside the Data folder:
 ### the *conts.csv* file:
   this file is the container file, these values denote the box u wanna pack all the meshes inside.
       this file is used by *construct.py*
       u can change the values for width, height and length inside
       width is x, height is y , length is z
      
 ### the *boxes.csv* file:
   this file is autogenerated by *construct.py*, u don't create nor change it but u can look inside it to gain some insight.
       this file holds info about the meshes dimensions aggregated for the pc to understand.
       
 ### the *mesh.csv* file:
   this file is autogenerated by *mesh.py* and used by *Pack.py*, 
   u don't create nor change it but u can look inside it to gain some insight.
   this file holds info about the  meshes dimensions aggregated for blender to understand.
 
  

## Inside the Executables folder:
   ### inside the *construct* file: 
there is a variable called `Mesh_No` : you don't have to count the number of meshes in the Mesh folder, just put the number of the last mesh + 1 , for instance my last mesh was 11.stl so i put `Mesh_No = 12`

   ### inside the *mesh* file: 
variable `x_Tolerance` : u can change it to values like 1, 1.3, 1.5 or whatever , this value governs the distance between meshes in the x-axis so u can make them touch or even join higher is joining them more. 

variable `y_Tolerance` : u can change it to values like 1, 1.3, 1.5 or whatever , this value governs the distance between meshes in the y-axis so u can make them touch or even join higher is joining them more.

variable `z_Tolerance` : u can change it to values like 1, 1.3, 1.5 or whatever , this value governs the distance between meshes in the z-axis so u can make them touch or even join higher is joining them more. 

variable `z_axis` : z_axis was throwing me off in the visualization so i added the option to disable it, u can enable it `z_axis = True` . 
  
 

## Inside the finale folder:
        ### combined.stl file :
             u can import it into blender, it is autogenerated by the script containing all the combined meshes. 
