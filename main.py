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
    print("\n STEP 1 : \n")
    git_1 = GitObject("config.ini", "GoogleColabTesting" ,"temp1") ## Creating an object  
    print("\n STEP 2 : \n")
    git_1.list_all_dir() ## List of things present in the current dir  
    print("\n STEP 3 : \n")
    git_1.mk_dir("temp1") ## Making a new dir given path
    print("\n STEP 4 : \n")
    git_1.mk_dir("temp2") ## Making a new temp dir to transfer the contents of the temp1
    print("\n STEP 5 : \n")
    git_1.clone_to_path() ## Cloning directory to destination variable
    print("\n STEP 6 : \n")
    #git_1.del_loc("temp1") ## Del temp1
    git_1.mv_to_loc("temp1/","temp2") ##
    
    #git_1.clone_to_path()
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
    