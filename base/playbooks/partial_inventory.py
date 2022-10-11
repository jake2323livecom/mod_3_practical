#!/usr/bin/env python3

import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Task 2, Step 1 - Build API call variables
NAUTOBOT_TOKEN = None
DEVICES_API_URL = None
METHOD = None
HEADERS = None
PARAMETERS = None


# Task 2, Step 2 - Execute the API call
devices = None
devices_json = None


# Task 2, Step 3 - Add hosts to hostvars
hostvars = {
    '_meta': {
        'hostvars': {}
    }
}


# Task 2, Steps 4 and 5
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



# Task 2, Step 6


# Task 2, Step 7 - Combine inventory components into one variable
inventory = None


# Step 8 - Print JSON inventory
