#!/usr/bin/env python3

# Task 2, Step 1
import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Task 2, Step 2 - Build API call variables
NAUTOBOT_TOKEN = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
DEVICES_API_URL = 'https://demo.nautobot.com/api/dcim/devices/'
METHOD = 'GET'
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Token {NAUTOBOT_TOKEN}'
}
PARAMETERS = {
    'site': 'ams01'
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
    if device['primary_ip4']:
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

    if 'red' in hostname:
        groups['red_devices']['hosts'].append(hostname)

    if 'yellow' in hostname:
        groups['yellow_devices']['hosts'].append(hostname)

    if 'ROUTER' in hostname:
        groups['routers']['hosts'].append(hostname)

    if 'SWITCH' in hostname:
        groups['switches']['hosts'].append(hostname)


# Task 2, Step 7
for group_name in groups.keys():
    if group_name != 'all':
        groups['all']['children'].append(group_name)


# Task 2, Step 8 - Combine inventory components into one variable
inventory = {}
inventory.update(hostvars)
inventory.update(groups)


# Task 2, Step 9 - Print JSON inventory
print(json.dumps(inventory, indent=4))