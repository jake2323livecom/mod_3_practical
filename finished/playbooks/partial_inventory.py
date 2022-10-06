#!/usr/bin/env python3

import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Step 1 - Build API call variables
NAUTOBOT_TOKEN = '89290b6b9df1226fa76fac388c3dc3f6a2a56d48'
DEVICES_API_URL = 'https://10.10.44.21/api/dcim/devices'
METHOD = 'GET'
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Token {NAUTOBOT_TOKEN}'
}
PARAMETERS = {
    'site': 'orko_mod_3_practical'
}

# Step 2 - Execute the API call
devices = requests.request(method=METHOD, url=DEVICES_API_URL, headers=HEADERS, params=PARAMETERS, verify=False)
devices_json = devices.json()

# Step 3 - Add hosts to hostvars
hostvars = {
    '_meta': {
        'hostvars': {}
    }
}

for device in devices_json['results']:
    hostvars['_meta']['hostvars'].update(
        {
            device['name']: {
            'ansible_host': device['primary_ip4']['address'].split('/')[0],
            'device_type': device['device_type']['model'],
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

# Step 4 and 5
for device in hostvars['_meta']['hostvars'].keys():
    if 'RED' in device:
        groups['red_devices']['hosts'].append(device)

    if 'YELLOW' in device:
        groups['yellow_devices']['hosts'].append(device)

    if 'ROUTER' in device:
        groups['routers']['hosts'].append(device)

    if 'SWITCH' in device:
        groups['switches']['hosts'].append(device)

# Step 6
for group in groups.keys():
    if group != 'all':
        groups['all']['children'].append(group)

    

# Step 7 - Combine inventory components into one variable
inventory = {}
inventory.update(hostvars)
inventory.update(groups)

# Step 8 - Print JSON inventory
print(json.dumps(inventory, indent=4))