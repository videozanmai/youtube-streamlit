import configparser

conf = configparser.ConfigParser()
conf.read('setting.ini')
APIPassword=conf['aukabu']['APIPassword']
Token=conf['aukabu']['Token']
Password=conf['aukabu']['Password']
