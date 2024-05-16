import yaml
import pyeapi
import uuid

pyeapi.load_config('eapi.conf')


# config_file = []
# with open('configs/borderleaf1.cfg') as f:
#     config_file = f.read().splitlines()

# config_file.append("\nx04")

file = open('configs/borderleaf1.cfg', 'r')
config_file = file.read()
# config_file = config_file+"\n\x04\n"
# config_file.append("\x04")
# print(config_file)
# config_file = "alias new2 show ip interface brief"

connect = pyeapi.connect_to('borderleaf1')
connect.enable([f"{config_file}"])
# # )# # connect.running_config = file

