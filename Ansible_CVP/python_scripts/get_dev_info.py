from cvprac.cvp_client import CvpClient

CVP_HOST = "192.168.0.5"
CVP_USER = "arista"
CVP_PWD = "arista5ufc"

clnt = CvpClient():
clnt.connect([CVP_HOST], CVP_USER, CVP_PWD), protocol='https')

print(clnt.get_devices())