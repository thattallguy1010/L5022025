import yaml
import pyeapi
import uuid
import difflib

pyeapi.load_config('eapi.conf')

# Config as a list
# config_file = []
# with open('configs/borderleaf1.cfg') as f:
#     config_file = f.read().splitlines()


# connect = pyeapi.connect_to('borderleaf1')
# old_config = connect.get_config()

# print(old_config)

# for line in difflib.unified_diff( 
#         config_file, old_config, lineterm=''): 
#     print(line) 

# print('n'.join(diff))
# # # config_file.append("\nx04")

# Config as a string
file = open('configs/borderleaf1.cfg', 'r')
config_file = file.read()


# # config_file = config_file+"\n\x04\n"
# # config_file.append("\x04")
# # print(config_file)
# # config_file = "alias new2 show ip interface brief"
uuid_id = uuid.uuid4()
connect = pyeapi.connect(host='borderleaf1', username='automator', password='arista123', transport='https')
connect.execute([f"configure session {uuid_id}",{"cmd":"copy terminal: session-config","input": config_file},"commit"])
