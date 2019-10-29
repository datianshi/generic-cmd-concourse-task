import yaml
import os

config = yaml.load(os.environ['config'])
cmds=[]
for cred in config['credentials']:
    bashCommand = "USERNAME={} PASSWORD={} HOST={} {}".format(cred['username'],cred['password'],cred['host'],config['command']['exec'])
    for arg in config['command']['argument']:
        bashCommand = bashCommand + " " + arg
    cmds.append(bashCommand)
for cmd in cmds:
    os.system(cmd)
