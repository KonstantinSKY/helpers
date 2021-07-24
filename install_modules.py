# Util for install needed python modules
from os_wrap import bash

input('-= Util for install needed python modules. Push any key. =-')

print('update pip...')
bash('pip install --upgrade pip')

with open('needed', 'r') as file:
    modules = file.read().split('\n')

modules = list(filter(lambda x: x != "" and x != " " and x.isspace, modules))
input(f'Will be installed next modules:  {modules}')

for module in modules:
    print("Installing:", module)
    bash(f'pip install {module}')

print("Installed!")
help('modules')
