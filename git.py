# Helper for git, to use it quickly

from os_wrapper import bash, subproc
import os
import sys


def delete():
    file = input("Press Enter file name for deleting: ")

    if file == '':
        print(f'File name is empty not exist')
        exit()
    bash(f'git rm {file}')
    commit(file)


def add():
    if input("Press Enter for continue 'git add *'  or Any key for exit") != "":
        exit()
    bash('git add *')
    commit()


def commit(msg=None):
    bash('git status')
    print("Committing and Pushing")
    if msg is None:
        msg = input("Enter commit message 'git commit -m' \n")
        if msg == "":
            bash('git commit -m "NO MESSAGE"')
        else:
            bash(f'git commit -m "{msg}"')
    else:
        bash(f'git commit -m "Deleting file: {msg}"')


if __name__ == "__main__":
    print("-" * 100)
    print(" -= GIT helper =- ")
    directory = os.path.abspath(os.curdir)
    print("Path for Git:", directory)
    print("-" * 100)

    p = subproc("git status").replace("\\n", "\n").replace("\\t", "\t").replace("\\'", "\'")
    print(p)
    if p.find("working tree clean") >= 0:
        print("WORKING TREE IS CLEAN!! QUIT")
        quit()

    print("-" * 100)

    if len(sys.argv) == 2 and sys.argv[1] == 'del':
        delete()
    else:
        add()

    bash('git push')
    bash('git status')
