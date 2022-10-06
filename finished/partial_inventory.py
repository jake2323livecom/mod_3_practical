#!/usr/bin/env python3

# Step 8 - Print the inventory in JSON format
import requests
import urllib3

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
devices = requests.request(method=METHOD, url=DEVICES_API_URL, headers=HEADERS, params=PARAMETERS)
devices_json = devices.json()

# Step 3 - Add hosts to hostvars
hostvars = {
    '_meta': {
        'hostvars': {}
    }
}

# Steps 4, 5, and 6
groups = {
    'all': {

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

# Step 7 - Combine inventory components into one variable
inventory = None

