# module for system command wrapper
import os
import sys
import subprocess


# just system command
def bash(command):
    print("System command: ")
    print('\033[92m ' + command + "\033[0m")
    os.system(command)


# subprocess with return string
def subproc(command):
    print("System command: ")
    print('\033[92m ' + command + "\033[0m")
    return str(subprocess.check_output(command, shell=True)).lstrip("'b/'").rstrip("'")


# Checking for Directory existing and create if not exist

def check_create_dir(path):
    if not os.path.exists(path) or not os.path.isdir(path):
        print(f'{path} - directory not found. It will be created automatically.')
        os.mkdir(path)
        return True



if __name__ == "__main__":
    bash('ls')
    print(subproc('ls -la'))
