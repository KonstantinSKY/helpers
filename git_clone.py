# Util for git clone and add necessary files
import os, shutil

print('-= Util for git clone and add necessary files =-')
print(f'Working directory will be created right here:{os.getcwd()}')
link = input('Enter the SSH link of repository and Push any key...\n')
directory = link[link.find('/')+1:-4]
# TODO check fo directory and rename
print(f'Will be created new directory: {os.getcwd}/{directory}')
# TODO add copy gitignore and create needed
# os.system(f'git clone {link}')
# print("Done")
# print('copying .gitignore file...')
# shutil.copy(/home/sky/Projects/test.txt", "D:\\folder")

