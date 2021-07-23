"""helper for configuring"""

from configparser import ConfigParser
import os

ConfigDirPath = 'config'


class Conf(ConfigParser):
    def __init__(self, name):
        super().__init__()
        self.optionxform = str
        self.path = ConfigDirPath+'/'+os.path.basename(name).split('.')[0]+'.conf'

        if not os.path.exists(ConfigDirPath) or not os.path.isdir(ConfigDirPath):
            print('Config directory not found. It will be created automatically.')
            os.mkdir(ConfigDirPath)

        if not os.path.exists(self.path) or not os.path.isfile(self.path):
            print('Config file '+self.path+' not found. It will be created automatically. ')
            self['DEFAULT'] = {'TestSettings': 'YES'}
            with open(self.path, "w+") as file:
                file.write(f"### Config file for {name}. Created automatically.\n\n")
                self.write(file)

        self.read(self.path)

    def save(self):
        with open(self.path, "w+") as file:
            self.write(file)

    def chk_add_key_data(self, key: str, data: dict):
        if key not in self:
            self[key] = data
            self.save()
            return

        for option in data:
            if option not in self[key]:
                self[key][option] = data[option]
        self.save()


if __name__ == "__main__":
    print("test2")
    configg = Conf('testname.py')
    print(os.getcwd())
    configg.read('config/testname')
    print(configg)

    print(configg['DEFAULT']['TestSettings'])
    # for key in configg:
    #     print(key)
    configg.chk_add_key_data('LOGGER', {'dfsd': 'sdfsdf'})
