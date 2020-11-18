from github import Github
from os.path import join  # import join used to join ROOT path and MY_GOOGLE_DRIVE_PATH
import subprocess
from configparser import ConfigParser


def ConfigReader():
    file = "/content/drive/My Drive/Projects/Config/config.ini"
    config = ConfigParser()
    config.read(file)
    return config


class GitObject:
    def __init__(self, PATH_TO_CONFIG=None, REPO=None, LocalPath=None):
        print("Starting GitObject Initialized")
        self.Repository = REPO
        self.local = LocalPath
        config = ConfigParser()
        config.read(PATH_TO_CONFIG)
        self.user = config["GitHub"]["USERNAME"]
        self.token = config["GitHub"]["TOKEN"]
        print("GitObject Initialized Completed")
        self.printing_values()

    def printing_values(self):
        print("*" + ("-" * 50) + "*")
        print("Repository Accessd : ", self.Repository)
        print("Local_path Accessd : ", self.local)
        print("User Accessd : ", self.user)
        print("Token Accessd : ", self.token)
        print("*" + ("-" * 50) + "*")

    def run(*args):
        return subprocess.check_call(["git"] + list(args))

    def clone():

        print("\nYou will be asked for the user first and then the repository name\n")

        user = input("User: ")
        __user__ = f"{user}"
        repo = input("Repository: ")
        __repo__ = f"{repo}"

        print("\nChoose the local path for your clone.")
        local = input("Local path: ")
        local_path = f"{local}"

        subprocess.Popen(
            [
                "git",
                "clone",
                "https://github.com/" + __user__ + "/" + __repo__ + ".git",
                local_path,
            ]
        )

    def commit(message):

        message = input("\nType in your commit message: ")
        commit_message = f"{message}"

        run("add", ".")
        run("commit", "-m", commit_message)
        run("push", "-u", "origin", "master")

    def branch(branch):
        """Type in the name of the branch you want to make:"""

        br = f"{branch}"

        run("checkout", "-b", br)

        choice = input("\nDo you want to push the branch right now to GitHub? (y/n): ")
        choice = choice.lower()

        if choice == "y":
            run("push", "-u", "origin", br)

        elif choice == "n":
            print("\nOkay, goodbye!\n")

        else:
            print("\nInvalid command! Use y or n.\n")


def main():
    git_1 = GitObject("config.ini", "GitUtils")
    # git_1.printing_values()


main()
