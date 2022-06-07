import os
import shutil
import time
path=input("Enter path: ")

list_files=os.listdir(path)

for file in list_files:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    

    if ext=="":
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)      
            
    
