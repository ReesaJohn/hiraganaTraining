import os
import re
import shutil

def getFolderName(string):
    ignorePart = re.compile(r"(kana|\d|.jpg)")
    return re.sub(ignorePart,"",string)

def create_folders(path):

    for i in os.listdir(path):
        current_folder = getFolderName(i)
        if os.path.exists(current_folder):
            print(path + "/" +i)
            print(current_folder+"/"+i)
            shutil.copy( path + "/" +i,current_folder+"/"+i)
        else:
            os.mkdir(current_folder)
            print(path + "/" + i)
            print(current_folder + "/" + i)
            shutil.copy(path + "/" + i, current_folder + "/" + i)
create_folders("hiragana_images")