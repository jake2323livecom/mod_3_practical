#!/usr/bin/env python3

import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Step 1 - Build API call variables
NAUTOBOT_TOKEN = None
DEVICES_API_URL = None
METHOD = None
HEADERS = None
PARAMETERS = None

# Step 2 - Execute the API call
devices = None
devices_json = None

# Step 3 - Add hosts to hostvars
hostvars = {
    '_meta': {
        'hostvars': {}
    }
}


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


# Step 6


# Step 7 - Combine inventory components into one variable
inventory = None


# Step 8 - Print JSON inventory
