import ConfigParser

conf_file = 'nsweeper.cfg'

config = ConfigParser.RawConfigParser()

config.read(conf_file)

def reset():
    pass

def getval(var):
    pass
    #return config.getboolean('Settings', var)

def conf_write():
    with open(conf_file, 'wb') as configfile:
        config.write(configfile)
