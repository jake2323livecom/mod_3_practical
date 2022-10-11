#!/usr/bin/env python3

# Task 2, Step 1


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Task 2, Step 2 - Build API call variables
NAUTOBOT_TOKEN = None
DEVICES_API_URL = None
METHOD = None
HEADERS = None
PARAMETERS = None


# Task 2, Step 3 - Execute the API call
devices = None
devices_json = None


hostvars = {
    '_meta': {
        'hostvars': {}
    }
}

# Task 2, Step 4 - Add hosts to hostvars


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

# Task 2, Steps 5 and 6


# Task 2, Step 7


# Task 2, Step 8 - Combine inventory components into one variable
inventory = None


# Task 2, Step 9 - Print JSON inventory
