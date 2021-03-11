# Helper for git, to use it quickly

import os
import sys
import subprocess


def bash(command):
    print('\033[92m ' + command + "\033[0m")
    os.system(command)


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


print("-" * 100)
print(" -= GIT helper =-")
directory = os.path.abspath(os.curdir)
print("Path for Git:", directory)
print("-" * 100)

p = str(subprocess.check_output("git status", shell=True)).lstrip("'b/'").rstrip("'").replace("\\n", "\n") \
    .replace("\\t", "\t").replace("\\'", "\'")
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
