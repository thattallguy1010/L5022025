from cvprac.cvp_client import CvpClient

CVP_HOST = "192.168.0.5"
CVP_USER = "arista"
CVP_PWD = "aristaeffq"

clnt = CvpClient()
clnt.connect([CVP_HOST], CVP_USER, CVP_PWD, protocol='https')

devices = clnt.get('/inventory/devices')
containers = clnt.get('/inventory/containers')

for container in containers:
    name = container.get('Name')
    print(f"Container Name: {name}")

for device in devices:
    hostname = device.get('hostname')
    ip_address = device.get('ipAddress')
    serial_number = device.get('serialNumber')
    model = device.get('modelName')
    mac = device.get('systemMacAddress')
    print(f" - Hostname: {hostname}, IP: {ip_address}, Serial: {serial_number}, Model: {model}, Mac: {mac}")

