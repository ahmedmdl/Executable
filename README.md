So i have seperated this into different folders so i can work , upload to the website and u just pull everyday to get the latest version.
# First step
Make a folder with any name u want, go inside,

make 3 files named `Data` `Finale` `Mesh`,

then do `git clone https://github.com/ahmedmdl/Executable`.

You should get the *Executable* folder now.

# Operation theory
`Construct.py` is the algorithm that looks inside the *Mesh* folder and reads all the meshes then converts them into a form that *Pack.py* can read , its output is *Boxes.csv* .

You can look into *Boxes.csv* to gain insight about dimensions but do not change it.
You can change the values for width, height and length inside the *conts.csv* file.

`Pack.py` is the algorithm that takes *Boxes.csv* and *Conts.csv* and calculates the ideal way to pack meshes into the container, its output is *Mesh.csv* .

`mesh.py` is the algorithm that takes *Mesh.csv* and converts it into a form that blender can read,its output is a numbered stl file and txt file having the the values of *x_Tolerance*, *y_Tolerance*, *z_Tolerance*, *z_axis* as a reminder for later comparison.

You can change *x_Tolerance*, *y_Tolerance*, *z_Tolerance*, *z_axis* values inside *mesh.py*, please check the *mesh.py section below.

Everyday u wake up and want to try , do `git pull`,and u will get my latest updates.



## Operation instructions
`python3 Construct.py`

`python3 Pack.py`

`python3 mesh.py`

Then check the finale folder, u can use blender to open it 

# Concept
## Inside the Mesh folder:
  Put as much meshes as u can with their names starting from *1.stl* just incrementing the number.
  
  in case meshes are not named in this way, you could just put whatever you want inside the folder then you will find inside the *Executables* folder a file named *rename_script.sh*, just execute it and it will rename everything automatically.
  
  You can put high res meshes as well and i encourage that.


## Inside the Data folder:
 ### The *conts.csv* file:
   This file is the container file, these values denote the box u wanna pack all the meshes inside.
   
   This file is used by *Pack.py*
   
   u can change the values for width, height and length inside
   
   width is x, height is y , length is z
      
 ### The *boxes.csv* file:
   This file is autogenerated by *construct.py*, 
   
   u don't create nor change it but u can look inside it to gain some insight.
   
   This file holds info about the meshes dimensions aggregated for the pc to understand.
       
 ### The *mesh.csv* file:
   This file is autogenerated by *Pack.py* and used by *mesh.py*,
   
   you don't create nor change it but u can look inside it to gain some insight.
   
   This file holds info about the  meshes dimensions aggregated for blender to understand.
 
  

## Inside the Executables folder:

   ### Inside the *mesh* file: 
Variable `x_Tolerance` : u can change it to values like 1, 1.3, 1.5 or whatever , this value governs the distance between meshes in the x-axis so u can make them touch or even join higher is ,joining them more. 

Variable `y_Tolerance` : u can change it to values like 1, 1.3, 1.5 or whatever , this value governs the distance between meshes in the y-axis so u can make them touch or even join higher is ,joining them more.

Variable `z_Tolerance` : u can change it to values like 1, 1.3, 1.5 or whatever , this value governs the distance between meshes in the z-axis so u can make them touch or even join higher is ,joining them more. 

Variable `z_axis` : z_axis was throwing me off in the visualization so i added the option to disable it, u can enable it `z_axis = True` . 
  
 

## Inside the finale folder:
### Combined.stl file :
   You can import it into blender, it contains all the combined meshes.
   
   it is autogenerated by the script. 
