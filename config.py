"""helper for configuring"""

from configparser import ConfigParser
import os
import os_wrap

ConfigDirPath = 'config'


class Conf(ConfigParser):
    def __init__(self, name):
        super().__init__()
        self.optionxform = str
        self.path = ConfigDirPath+'/'+os.path.basename(name).split('.')[0]+'.conf'

        os_wrap.check_create_dir(ConfigDirPath)

        if not os.path.exists(self.path) or not os.path.isfile(self.path):
            print('Config file '+self.path+' not found. It will be created automatically. ')
            self['DEFAULT'] = {'TestSettings': 'YES'}
            with open(self.path, "w+") as file:
                file.write(f"### Config file for {name}. Created automatically.\n\n")
                self.write(file)

        self.read(self.path)

    def save(self):                             # save config to file
        with open(self.path, "w+") as file:
            self.write(file)

    def chk_add_key_data(self, key: str, data: dict):   # check and add options to keq if necessary
        if key not in self:
            self[key] = data
            self.save()
            return

        for option in data:
            if option not in self[key]:
                self[key][option] = data[option]
        self.save()


if __name__ == "__main__":
    print("test for config module")
    config = Conf('testname.py')
    config.read(f'{ConfigDirPath}/testname')
    print(config)

    print('TestSetting:', config['DEFAULT']['TestSettings'])

    print('all keys in config:')
    for key in config:
        print(key)

    config.chk_add_key_data('LOGGER', {'dfsd': 'sdfsdf'})
