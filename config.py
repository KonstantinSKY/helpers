import configparser
import os

ConfigDirPath = 'config'
logger = 'logger.conf'

print("test")

config = configparser.ConfigParser()
config.optionxform = str

if not os.path.exists(ConfigDirPath) or not os.path.isdir(ConfigDirPath):
    print('Config directory not found')
    os.mkdir(ConfigDirPath)

path = ConfigDirPath+'/'+logger
if not os.path.exists(path) or not os.path.isfile(path):
    print('Config file '+path+' not found')



    config['NO_PRINT'] = {"AllLogs": 'ЫВАeq',
                      'IL': '234',
                      'ErrLogs': False}
    config['NO_PRINT']['DfdDdfd'] = 'FGH'

    conf = {"AllLoDFgs": 'ЫВАdeq', 'ILdf': '234', 'ErrDDDDDLogs': False, 'DfdDdfd': 'FGH'}

    print(conf)

for key in config['NO_PRINT']:
    print(key)

with open('logger.conf', 'w') as configfile:
    config.write(configfile)


if __name__ == "__main__":
    print("test2")
    print(config['NO_PRINT'])
    print(config)
    print(config.sections())
    for key in config['NO_PRINT']:
        print(key)
