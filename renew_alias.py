# Util for renew my aliases data
from os_wrapper import bash
from os.path import expanduser


print('\n -= Util for renew my aliases data =- \n')
home_dir = expanduser("~")+'/'

with open(home_dir + 'Projects/Settings/aliases', 'r') as file:
    new_aliases = file.read()

with open(home_dir + '.bashrc', 'r+') as file:
    bashrc = file.read()
    print("Old bashrc...")
    print(bashrc)
    bashrc = bashrc[0: bashrc.find('my aliases') - 1] + new_aliases
    print("NEW bashrc...")
    print(bashrc)
    file.write(bashrc)

print('Done!')
