import time,os,shutil
from typing import final

days=int(input("Enter the number of days file should be older than: "))
path = input("Enter the path : ")+"/"
statTime=time.time()
seconds = statTime-days*24*60*60

path_exists=os.path.exists(path)

if path_exists :
    deletedFolders = 0
    deletedFiles = 0

    for (root,dirs,files) in os.walk(path):
        if seconds>=os.stat(root).st_ctime :
            deletedFolders+=1
            shutil.rmtree(root)
            break
        else :
            for folder in dirs :
                folderPath=os.path.join(root,folder)
                if seconds>= os.stat(folderPath).st_ctime :
                    deletedFolders+=1
                    shutil.rmtree(folderPath)
                    
            for file in files :
                filePath=os.path.join(root,file)
                if seconds>= os.stat(filePath).st_ctime :
                    deletedFiles+=1
                    os.remove(filePath)
    
    print("Total number of deleted folders :",deletedFolders)
    print("Total number of deleted files :",deletedFiles)


else : 
    print("Path doesn't exist")