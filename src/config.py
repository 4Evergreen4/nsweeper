import ConfigParser

conf_file = 'nsweeper.cfg'

config = ConfigParser.RawConfigParser()

config.read(conf_file)

def reset():
    pass

def getval(var, section):
    config.read(conf_file)
    return config.get(section, var)

def conf_write():
    with open(conf_file, 'wb') as configfile:
        config.write(configfile)
