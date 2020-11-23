from github import Github
from os.path import join  # import join used to join ROOT path and MY_GOOGLE_DRIVE_PATH
import subprocess
from configparser import ConfigParser
import os
from os.path import join
import shutil


class GitObject:
    def __init__(self, PATH_TO_CONFIG=None, REPO=None, dest=""):
        print("Starting GitObject Initialized")
        self.parent_dir = str(os.getcwd())
        self.Repository = REPO
        self.dest = self.abs_path(dest)
        config = ConfigParser()
        config.read(PATH_TO_CONFIG)
        self.user = config["GitHub"]["USERNAME"]
        self.token = config["GitHub"]["TOKEN"]
        self.curr_dir = os.getcwd()
        print("GitObject Initialized Completed")
        self.printing_values()

    def printing_values(self):
        print("*" + ("-" * 100) + "*")
        print("Repository Accessd : ", self.Repository)
        print("User Accessd : ", self.user)
        print("Token Accessd : ", self.token)
        print("Destination_Path : ", self.dest)
        print("Parent Wk_dir :", self.parent_dir)
        print("Current Working Dir :", self.curr_dir)
        print("*" + ("-" * 100) + "*")

    def run(*args):
        return subprocess.call(["git"] + list(args))

    def abs_path(self, path):
        return join(self.parent_dir, path)

    def list_all_dir(self):
        """ See the list of all dir tree"""
        curr_wk_dir = f"{str(os.getcwd())}"
        print(
            "listing all files and directories under working directory :",
            curr_wk_dir,
            " -- ",
        )
        print(os.listdir())

    def mk_dir(self, dir_name):
        """ See the list of all dir tree"""
        curr_wk_dir = f"{str(os.getcwd())}"
        dir_path = join(curr_wk_dir, dir_name)
        print("Creating a new directory in the following path :", dir_path, " -- ")

        try:
            os.mkdir(dir_path)
        except OSError as error:
            print(error, " , Moving on with the process")

    def cd_to_loc(self, loc):
        """ Switch your Working Directory """
        loc = f"{loc}"
        # print("Seting Working dir as :", loc)
        # print(["cd", loc])

        chg_dir = join(self.parent_dir, loc)
        print("Parent Dir : ", self.parent_dir)
        print("dir to be changed to :", chg_dir)
        os.chdir(chg_dir)
        self.curr_dir = f"{str(os.getcwd())}"

    def del_loc(self, loc):
        """ See the list of all dir tree"""
        __loc__ = f"{loc}"
        rm_dir = join(self.parent_dir, __loc__)
        print("Removing directory :: ", rm_dir)
        shutil.rmtree(rm_dir)
        # self.dest = None

    def clone_to_path(self):
        """ Function to clone the repository to a particular local path :: """

        dest_path = f"{self.dest}"
        print("\nCloning git to path : ", dest_path)

        user = self.user
        __user__ = f"{user}"
        repo = self.Repository
        __repo__ = f"{repo}"
        token = self.token
        __token__ = f"{token}"

        dest_path = f"{self.dest}"

        subprocess.run(
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
        os.chdir(self.dest)
        commit_message = f"{message}"

        subprocess.run(["git","add", "."])
        subprocess.run(["git","commit", "-m",commit_message])
        print("Commited all the changes successfully")
        os.chdir(self.parent_dir)
        # run("push", "-u", "origin", "master")

    def push(self, branch_name):
        """ Function to stage and commit changes to an particular repo after making changes """
        os.chdir(self.dest)
        br = f"{branch_name}"

        # message = input("\nType in your commit message: ")
        #commit_message = f"{message}"
        subprocess.run(["git","push", "origin",br])
        os.chdir(self.parent_dir)

    def create_new_branch(self, branch):
        """Create a new branch  """
        os.chdir(self.dest)
        br = f"{branch}"

        subprocess.run(["git" , "checkout", "-b", br])
        print("Created Branch ", br, "successfully")
        os.chdir(self.parent_dir)

    def switch_branch(self, branch):
        """Switch between branches """
        os.chdir(self.dest)
        br = f"{branch}"

        subprocess.run(["git","checkout", br])
        print("Switched Branch to", br, "successfully")
        os.chdir(self.parent_dir)

    def git_to_local(self):
        """Create a new branch and commit and push the changes into them """
        print("Function Under dev")

    def mv_to_loc(self, source, dest):
        """ Copy the contents of cloned dir to wk """
        dest = f"{self.abs_path(dest)}"

        source = f"{self.abs_path(source)}"
        os.chdir(source)
        files = os.listdir()

        print("Moving the contents of cloned dir to wk")
        for file in files:
            __source__ = join(source, file)
            __dest__ = join(dest, file)
            print("Moving file :", file)
            try:
                shutil.copy(__source__, __dest__, follow_symlinks=False)
                print("File copied successfully.")

            # If source and destination are same
            except shutil.SameFileError:
                print("Source and destination represents the same file.")
            except PermissionError:
                print("Permission denied.")

            # For other errors
            except:
                print("Error occurred while copying file.")
            # print("Moved to :" , result ,"\n")
        os.chdir(self.parent_dir)    

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
        subprocess.run(["rsync", "-aPz", __exclude_list__, __source__, __dest__])


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
