# Util for git clone and add necessary files
from os_wrap import bash
import os
import shutil

home_dir = os.path.expanduser("~")+'/'
settings_dir = home_dir + "Projects/Settings/"

print('\n -= Util for git clone and add necessary files =- \n')


print(f'Working directory will be created right here:{os.getcwd()}\n')

with open(settings_dir+'git_links', 'r') as file:
    links_list = list(filter(lambda x: x != "" and x != " " and x.isspace, file.read().split('\n')))

print("Select NUMBER of SSH git link for make the repo clone \n")

for num in enumerate(links_list):
    print(f'{num[0]} :  {num[1]}')

num = int(input('\n Input number: '))

if 0 < num <= len(links_list):
    link = links_list[num]
else:
    print("Link not found in list !!!\n")
    link = input('Enter the SSH link of repository and PUSH any key...\n')

print('\n Your choice is:', link)
directory = os.getcwd() + link[link.find('/'):-4]
print(f'\nWill be created new and working directory: {directory}')
if os.path.exists(directory):
    input(f'{directory} is exists. It will be rename to {directory}_old. Push any key to confirm')
    print(f'\nRenaming {directory}...', link)
    os.rename(directory, directory+'_old')
    print('\nRenamed...', link)

print(f'\nCloning the repository to working directory: {directory}')
bash(f' git clone {link}')

print("Copying .gitignore...")
gitignore_template = settings_dir + 'gitignore_template'
if os.path.exists(gitignore_template):
    shutil.copy(gitignore_template, directory+'/.gitignore')
else:
    print("gitignore_template not found and will not copy!!")

print("Copying requirements.txt...")

requirements = settings_dir + 'requirements.txt'
if os.path.exists(gitignore_template):
    shutil.copy(requirements, directory+'/requirements.txt')
else:
    print("requirements not found and will not copy!!")

print("Done")


