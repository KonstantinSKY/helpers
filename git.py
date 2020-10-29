import os
import sys


def bash(command):
    print('\033[92m '+command+"\033[0m")
    os.system(command)


def delete():
    pass


def add():
    if input("Press Enter for continue 'git add *'  or Any key for exit") != "":
        exit()
    bash('git add *')


def commit():
    bash('git status')
    print("Commiting and Pushing")
    msg = input("Enter commit message 'git commit -m' \n")
    if msg == "":
        bash(f'git commit -m NO MESSAGE')
    else:
        bash(f'git commit -m "{msg}"')


print(" -=GIT helper=-")
directory = os.path.abspath(os.curdir)
print("Path for Git:", directory)
print("-"*100)
bash('git status')
print("-"*100)

if len(sys.argv) == 2:
    delete()
else:
    add()

commit()
bash('git push')
bash('git status')




