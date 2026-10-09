from textnode import TextNode
import shutil
import os
def copy_static_files(source_path, dest_path, dest_cleaned= False):
    if not dest_cleaned:
        shutil.rmtree(dest_path)
        dest_cleaned = True
    list_of_names = os.listdir(source_path)
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    if not list_of_names:
        return
    for name in list_of_names:
        target_path = os.path.join(dest_path, name)
        name_path = os.path.join(source_path, name)
        if os.path.isfile(name_path):
            shutil.copy(name_path, target_path)
        else:
            copy_static_files(name_path, target_path, dest_cleaned)
        

def main():
    copy_static_files("./static","./public")

main()
