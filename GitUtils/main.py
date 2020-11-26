from EasyOS import GitObject 
import os

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
    print("\n STEP 1 : Creating the Object \n")
    git_1 = GitObject("config.ini", "GoogleColabTesting" ,"temp1") ## Creating an object  
    #print(os.getcwd())
    print("*" * 50 , "\n")
    print(git_1.user)
    git_1.printing_values()
    #print("\n STEP 2 : List of things present in the current dir  \n")
    #git_1.list_all_dir() ## List of things present in the current dir  
    #print("\n STEP 3 : Making a new dir given path\n")
    #git_1.mk_dir("temp1") ## Making a new dir given path
    #print(os.getcwd())
    
    #print("\n STEP 4 : Making a new temp dir to transfer the contents of the temp1\n")
    #git_1.mk_dir("temp2") ## Making a new temp dir to transfer the contents of the temp1
    #print(os.getcwd())

    #print("\n STEP 5 : Cloning directory to destination variable\n")
    #git_1.clone_to_path() ## Cloning directory to destination variable
    #print(os.getcwd())

    #print("\n STEP 6 : Moving the contents of temp1 to temp 2 \n")
    #git_1.del_loc("temp1") ## Del temp1
    
    #git_1.mv_to_loc("temp1/","temp2") ##
    #print(os.getcwd())

    #git_1.sync_to_wk(
    #    source="temp1/",
    #    dest="temp2",
    #    exclude_list={"data/", "sample/", "drive/", ".config/",".git/"},
    #)
    #print("STEP 7 : Make some changes to temp2 and store them in temp 1")
    #print(os.getcwd())

    #f = open("temp2/Switch_branch_Test.txt", "a")
    #f.write("Now the file has more content!")
    #f.close()
    
    #print(os.getcwd())
    #print("\n STEP 8 : Rsync temp2 contents to temp 1 -- \n ")
    #git_1.sync_to_wk(
    #    source="temp2/",
    #    dest="temp1",
    #    exclude_list={"data/", "sample/", "drive/", ".config/",".git/"},
    #)

    #print("\n STEP 9 : Crerating a new branch named test1 \n ")
    #git_1.create_new_branch("test1")
    #git_1.switch_branch("test1")
    #git_1.commit("Switch Branch Test using EasyOS Class")
    #git_1.push("test1")
    
    #print("STEP 7 : Creating Branches in a directory ")
        # make changes in the cloned dir and push the changes 


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
    