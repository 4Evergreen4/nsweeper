config_file = open('../nsweeper.conf', 'r')
configstr = config_file.read()

configlist = configstr.split('\n')

config_file.close()
