from github import Github
from os.path import join  # import join used to join ROOT path and MY_GOOGLE_DRIVE_PATH
import subprocess
from configparser import ConfigParser
import os
from os.path import join
import shutil


class GitObject:
    def __init__(self, PATH_TO_CONFIG=None, REPO=None, dest=None):
        print("Starting GitObject Initialized")
        self.Repository = REPO
        self.dest = dest
        config = ConfigParser()
        config.read(PATH_TO_CONFIG)
        self.user = config["GitHub"]["USERNAME"]
        self.token = config["GitHub"]["TOKEN"]
        self.parent_dir = str(os.getcwd())
        self.curr_dir = self.parent_dir
        print("GitObject Initialized Completed")
        self.printing_values()

    def printing_values(self):
        print("*" + ("-" * 100) + "*")
        
        print("Repository Accessd : ", self.Repository)
        print("User Accessd : ", self.user)
        print("Token Accessd : ", self.token)
        print("Destination_Path : ", self.dest)
        print("Parent Wk_dir :",self.parent_dir)
        print("Current Working Dir :",self.curr_dir)
        print("*" + ("-" * 100) + "*")

    def run(*args):
        return subprocess.check_call(["git"] + list(args))

    def clone_to_path(self):
        """ Function to clone the repository to a particular local path :: """

        dest_path = f"{self.dest}"
        print("\nCloning git to path : ", dest_path)

        user = self.user
        __user__ = f"{user}"
        repo = self.REPO
        __repo__ = f"{repo}"
        token = self.token
        __token__ = f"{token}"

        dest_path = f"{self.dest}"

        subprocess.Popen(
            [
                "git",
                "clone",
                "https://"
                + __token__
                + "@github.com/"
                + __user__
                + "/"
                + __repo__
                + ".git",
                dest_path,
                # GIT_PATH = "https://" + GIT_TOKEN + "@github.com/" + GIT_USERNAME + "/" + GIT_REPOSITORY + ".git"
            ]
        )

    def commit(self, message):
        """ Function to stage and commit changes to an particular repo after making changes """

        # message = input("\nType in your commit message: ")
        commit_message = f"{message}"

        run("add", ".")
        run("commit", "-m", commit_message)
        print("Commited all the changes successfully")
        # run("push", "-u", "origin", "master")

    def push(self, branch_name):
        """ Function to stage and commit changes to an particular repo after making changes """
        br = f"{branch_name}"

        # message = input("\nType in your commit message: ")
        commit_message = f"{message}"
        run("push", "origin", br)

    def create_new_branch(self, branch):
        """Create a new branch and commit and push the changes into them """

        br = f"{branch}"

        run("checkout", "-b", br)
        print("Created Branch ", br, "successfuully")

    def switch_branch(self, branch):
        """Switch between branches """

        br = f"{branch}"

        run("checkout", br)
        print("Switched Branch to", br, "successfuully")

    def git_to_local(self):
        """Create a new branch and commit and push the changes into them """
        print("Function Under dev")

    def mv_to_loc(self, source , dest ):
        """ Copy the contents of cloned dir to wk """
        dest = f"{dest}"

        source = f"{source}"
        print("Moving the contents of cloned dir to wk")
        subprocess.run(["mv", source, dest],shell=True)


    def sync_to_wk(
        self,
        source=None,
        dest=None,
        exclude_list={"data/", "sample/", "drive/", ".config/"},
    ):
        """ Copy the contents of cloned dir to wk """

        __source__ = f"{source}"
        __dest__ = f"{dest}"
        __exclude_list__ = "--exclude=" + f"{exclude_list}"

        print("rsync", "-aP", __exclude_list__, __source__, __dest__)
        print(
            "Syncing source and destination with source as ",
            __source__,
            "and destination as ",
            __dest__,
            "excluding ",
            exclude_list,
        )
        subprocess.run(["rsync", "-aP", __exclude_list__, __source__, __dest__])

    def list_all_dir(self):
        """ See the list of all dir tree"""
        curr_wk_dir = f"{str(os.getcwd())}"
        print(
            "listing all files and directories under working directory :", curr_wk_dir
        )
        print(os.listdir())

    def cd_to_loc(self, loc):
        """ See the list of all dir tree"""
        loc = f"{loc}"
        #print("Seting Working dir as :", loc)
        #print(["cd", loc])
        
        chg_dir = join(self.parent_dir , loc)
        print("Parent Dir : ",self.parent_dir)
        print("dir to be changed to :", chg_dir )
        os.chdir(chg_dir)
        self.curr_dir = f"{str(os.getcwd())}"
        
    def del_to_loc(self, loc):
        """ See the list of all dir tree"""
        __loc__ = f"{loc}"
        rm_dir = join(self.parent_dir , __loc__)
        print("Removing directory :: ",rm_dir)
        shutil.rmtree(rm_dir)
        print("Deleting destination file and setting self.dest --> None")
        #self.dest = None



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
    git_1.cd_to_loc("temp")
    git_1.list_all_dir()
    git_1.printing_values()
    source = "/Users/ramamurthi/Pet_Projects/GitUtils/temp/*"
    dest = "/Users/ramamurthi/Pet_Projects/GitUtils/"
    #git_1.mv_to_loc(source,dest)
    git_1.del_to_loc("temp")
    
    # git_1.sync_to_wk("source_path","dest_path")
    # git_1.printing_values()


main()
