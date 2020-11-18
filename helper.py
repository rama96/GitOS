from github import Github
from os.path import join # import join used to join ROOT path and MY_GOOGLE_DRIVE_PATH 
import subprocess
from configparser import ConfigParser

def run(*args):

    return subprocess.check_call(['git'] + list(args))

def clone():

    print("\nYou will be asked for the user first and then the repository name\n")

    user = input("User: ")
    __user__ = f'{user}'
    repo = input("Repository: ")
    __repo__ = f'{repo}'

    print("\nChoose the local path for your clone.")
    local = input("Local path: ")
    local_path = f'{local}'

    subprocess.Popen(['git', 'clone', "https://github.com/" + __user__ + "/" + __repo__ + ".git", local_path])

def commit():

    message = input("\nType in your commit message: ")
    commit_message = f'{message}'
    
    run("add", ".")
    run("commit", "-m", commit_message)
    run("push", "-u", "origin", "master")


def branch():

    branch = input("\nType in the name of the branch you want to make: ")
    br = f'{branch}'

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

    choices = 'clone, commit, branch, pull, merge, blame and stash'
    print("Commands to use: " + choices)

    choose_command = input("Type in the command you want to use: ")
    choose_command = choose_command.lower()

    if choose_command == "clone":
        clone()

    elif choose_command == "commit":
        commit()

    elif choose_command == "branch":
        branch()

    elif choose_command == "pull":
        pull()

    elif choose_command == "merge":
        merge()

    elif choose_command == "blame":
        blame()

    elif choose_command == "stash":
        stash()

    else:
        print("\nNot a valid command!")
        print("\nUse " + choices)


main()