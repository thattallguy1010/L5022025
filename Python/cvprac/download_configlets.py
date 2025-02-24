from cvprac import cvp_client as cvp_client
import requests
import os

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp1 = '192.168.0.5'
cvp_user = 'arista'
cvp_pw = 'arista5ufc'

client = cvp_client.CvpClient()

client.connect([cvp1], cvp_user, cvp_pw)

directory = 'configs'
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

configlets = client.api.get_configlets(start=0,end=0)

for configlet in configlets['data']:
    file = open(f"./{directory}/{configlet['name']}.txt", 'w')
    file.write(configlet['config'])
    file.close()