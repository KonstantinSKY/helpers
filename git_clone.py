# Util for git clone and add necessary files
import os

print('\n -= Util for git clone and add necessary files =- \n')
print(f'Working directory will be created right here:{os.getcwd()}\n')

# os.system(f'git clone {link}')
#
# print("Done")
# print('copying .gitignore file...')
# shutil.copy(/home/sky/Projects/test.txt", "D:\\folder")

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

print('\n Your choise: ', link)
directory = link[link.find('/'):-4]
print(f'\nWill be created new and working directory: {os.getcwd()}{directory}')
# os.system(f' git clone {link}')

print("Done")
print("Installed!")

