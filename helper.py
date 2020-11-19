from github import Github
from os.path import join  # import join used to join ROOT path and MY_GOOGLE_DRIVE_PATH
import subprocess
from configparser import ConfigParser
import os
from os.path import join
import shutil
from EasyOS import GitObject 


# Commands used in jupyter -- 
"""
    PROJECT_PATH_NEW = join(PROJECT_PATH,GIT_REPOSITORY)
    !mkdir "{PROJECT_PATH_NEW}"
    ### Cloning to a temp folder and making files accessable in the current workspace  
    !mkdir ./temp
    !git clone "{GIT_PATH}" ./temp
    !mv ./temp/* "{PROJECT_PATH_NEW}"
    !rm -rf ./temp
    !rsync -aP --exclude=data/ "{PROJECT_PATH_NEW}"/*  ./
    --exclude={'file1.txt','dir1/*','dir2'}
"""
# -- 

def main():
    git_1 = GitObject("config.ini", "GitUtils")
    git_1.list_all_dir()
    git_1.mk_dir("temp/temp1")
    git_1.del_loc("temp/temp1")
    #git_1.list_all_dir()
    #git_1.printing_values()
    #source = "/Users/ramamurthi/Pet_Projects/GitUtils/temp/*"
    #dest = "/Users/ramamurthi/Pet_Projects/GitUtils/"
    #git_1.mv_to_loc(source,dest)
    #git_1.del_to_loc("temp")
    
    # git_1.sync_to_wk("source_path","dest_path")
    # git_1.printing_values()

if __name__ == "__main__":
    main()
