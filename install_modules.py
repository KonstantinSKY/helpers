# Util for install needed python modules
import os
input('Util for install needed python modules. Push any key.')

print('update pip...')
os.system('pip install --upgrade pip')

with open('needed', 'r') as file:
    modules = file.read().split('\n')

modules = list(filter(lambda x: x != "" and x.isspace, modules))
input(f'Will be installed next modules:  {modules}')

for module in modules:
    print("Installing:", module)
    os.system(f'pip install {module}')

print("Installed!")
help('modules')
