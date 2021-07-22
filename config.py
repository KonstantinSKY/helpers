from configparser import ConfigParser
import config
import os

ConfigDirPath = 'config'

print("test")


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
        # print(self.path)
        # print(self.sections())


    #
# if not os.path.exists(ConfigDirPath) or not os.path.isdir(ConfigDirPath):
#     print('Config directory not found')
#     os.mkdir(ConfigDirPath)
#
# path = ConfigDirPath+'/'+logger
#
#
#     config['NO_PRINT'] = {"AllLogs": 'ЫВАeq',
#                       'IL': '234',
#                       'ErrLogs': False}
#     config['NO_PRINT']['DfdDdfd'] = 'FGH'
#
#     conf = {"AllLoDFgs": 'ЫВАdeq', 'ILdf': '234', 'ErrDDDDDLogs': False, 'DfdDdfd': 'FGH'}
#
#     print(conf)
#
# for key in config['NO_PRINT']:
#     print(key)
#
# with open('logger.conf', 'w') as configfile:
#     config.write(configfile)


if __name__ == "__main__":
    print("test2")
    # print(config['NO_PRINT'])
    # print(config)
    # print(config.sections())
    # for key in config['NO_PRINT']:
    #     print(key)
    configg = Conf('testname')
    print(os.getcwd())
    configg.read('config/testname')
    print(configg)
    # config = ConfigParser()
    # config.read('config/testname')
    # print(config.sections())
    print(configg['DEFAULT']['TestSettings'])
    for key in configg:
        print(key)
