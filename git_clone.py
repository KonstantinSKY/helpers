# Util for git clone and add necessary files
import os

print('\n -= Util for git clone and add necessary files =- \n')
print(f'Working directory will be created right here:{os.getcwd()}\n')

with open('/home/sky/Projects/Settings/git_links', 'r') as file:
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

print('\n Your choice is: ', link)
directory = os.getcwd() + link[link.find('/'):-4]
print(f'\nWill be created new and working directory: {directory}')
if os.path.exists(directory):
    input(f'{directory} in exists. It will be rename to {directory}_old. Push any key to confirm')
    os.rename(directory, directory+'_old')
    print('\nRenamed...', link)

print(f'\nCloning the repository to working directory: {directory}')
os.system(f' git clone {link}')

print("Done")
print("Remember to add files for setup working directory")

