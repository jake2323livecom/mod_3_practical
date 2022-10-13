#!/usr/bin/env python3

# Task 2, Step 1
import requests
import urllib3
import json


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Task 2, Step 2 - Build API call variables
NAUTOBOT_TOKEN = '89290b6b9df1226fa76fac388c3dc3f6a2a56d48'
DEVICES_API_URL = 'https://10.10.44.21/api/dcim/devices/'
METHOD = 'GET'
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Token { NAUTOBOT_TOKEN }'
}
PARAMETERS = {
    'site': 'orko_mod_3_practical'
}


# Task 2, Step 3 - Execute the API call
devices = requests.request(method=METHOD, url=DEVICES_API_URL, headers=HEADERS, params=PARAMETERS, verify=False)
devices_json = devices.json()


hostvars = {
    '_meta': {
        'hostvars': {}
    }
}

# Task 2, Step 4 - Add hosts to hostvars
for device in devices_json['results']:
    hostvars['_meta']['hostvars'].update(
        {
            device['name']: {
                'ansible_host': device['primary_ip4']['address'].split('/')[0],
                'device_type': device['device_type']['model']
            }
        }
    )


groups = {
    'all': {
        'children': []
    },
    'red_devices': {
        'hosts': []
    },
    'yellow_devices': {
        'hosts': []
    },
    'routers': {
        'hosts': []
    },
    'switches': {
        'hosts': []
    }
}

# Task 2, Steps 5 and 6 - Group hosts based on enclave and device type
for hostname in hostvars['_meta']['hostvars'].keys():
    if 'RED' in hostname:
        groups['red_devices']['hosts'].append(hostname)
    if 'YELLOW' in hostname:
        groups['yellow_devices']['hosts'].append(hostname)
    if 'ROUTER' in hostname:
        groups['routers']['hosts'].append(hostname)
    if 'SWITCH' in hostname:
        groups['switches']['hosts'].append(hostname)


# Task 2, Step 7
for group in groups.keys():
    if group != 'all':
        groups['all']['children'].append(group)


# Task 2, Step 8 - Combine inventory components into one variable
inventory = {}
inventory.update(hostvars)
inventory.update(groups)


# Task 2, Step 9 - Print JSON inventory
print(json.dumps(inventory, indent=4))
