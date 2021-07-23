from configparser import ConfigParser
import os

ConfigDirPath = 'config'


class Conf(ConfigParser):
    def __init__(self, name):
        super().__init__()
        self.optionxform = str
        self.path = ConfigDirPath+'/'+name

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


if __name__ == "__main__":
    print("test2")
    configg = Conf('testname')
    print(os.getcwd())
    configg.read('config/testname')
    print(configg)

    print(configg['DEFAULT']['TestSettings'])
    for key in configg:
        print(key)
