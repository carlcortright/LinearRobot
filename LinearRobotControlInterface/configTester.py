import config

config.printConfig()
config.readConfig()

print "\n"

config.printConfig()
config.speed = 0
config.camera = "Cannon EOS5"
config.writeConfig()

print "\n"
config.printConfig()