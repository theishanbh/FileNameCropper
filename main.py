import os

path_name = 'F:\Personal Project\FileNameCropper\Files' 
#insert path name where you want you to change 

path = os.chdir(path_name)
path_list = os.listdir(path)
for filename in path_list:
    seperator = "-" # the literal after which the chars will be removed
    filetype = ".mp3"
    new_name = "".join(filename.split(sep=seperator)[:-1])+filetype
    print(new_name)
    os.rename(filename, new_name)

