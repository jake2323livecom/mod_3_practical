# mod_3_practical

## Topics to cover:
- python
- api calls
- yaml/json
- ansible

# Build device configuration files with Ansible

# Task 1 - Preparation

<br/>

## Step 1 - Set up Remote-SSH

* Use Git Bash to send your windows laptops SSH public key to your lab VM.  
* Use the Remote-SSH extension in VS Code to open a session to your lab VM.

<br/>

## Step 2 - Clone the practical exam repository

* On your lab VM, generate an SSH key-pair.
* Add the new public key to your profile in Gitlab.
* Clone the exam repo to your lab VM using SSH and go into the top-level directory of the repo.
* Create a new branch from the _development_ branch, and name it `StudX-Practical`, where `X` is your personal student number.

<br/>

# Task 2 - Finish the `partial_inventory.py` dynamic inventory script

Each of the following steps will have you either complete a section or create code from scratch in the `partial_inventory.py` in the `ansible` directory.  Each of the following steps will correlate to an appropriately labeled comment within the script so that you will know what the directions are referencing.

<br/>

## Step 1 - Build API call variables

This script will execute an API call to the locally hosted Nautobot server.  The API call was intended to _retrieve_ the information for all devices that belong to the site `orko_mod_3_practical`.  You will need to fix the API call variables.

<br/>

* Login to the local Nautobot server at `https://10.10.44.21`.  There is already an account set up for you.  The username is `studX`, where `X` is your personal student number, and the password is `P@ssw0rd123!`.

<br/>

* Once logged in, open your account profile, and find your personal API token.  You will need it for the script.

<br/>

* Lines 10-14 will need to be completed by setting the constants to their appropriate values, excluding the `DEVICES_API_URL` constant which has already been defined for you.  You will need to set the values for these variables:

    * `NAUTOBOT_TOKEN`
    * `DEVICES_API_URL`
    * `METHOD`
    * `HEADERS`
    * `PARAMETERS`

<br/>

* The `NAUTOBOT_TOKEN` variable needs to be set to a string containing your personal API token.

<br/>

* The `DEVICES_API_URL` should be set to `'https://10.10.44.21/api/dcim/devices'`, which is the list view for all devices in the Nautobot server.

* The `METHOD` variable should be set to the appropriate HTTP method that is used when retrieving data only.

* The `HEADERS` variable should set three HTTP headers to the appropriate values for the Nautobot API:

    * `Accept`
    * `Content-Type`
    * `Authorization`

* The `PARAMETERS` variable should set a single parameter called `site` equal to `orko_mod_3_practical`.

## Step 2 - Execute the API call

* On line X, use the `requests` module to execute an API call that utilizes all of the variables that you just configured.  Save the result of this API into the `devices` variable.

* Then, on line X, set the `devices_json` variable to the _JSON_ data contained within the `devices` variable.

### If you'd like, you can test this API call in Thunderclient to make sure it works before attempting to run this script.

<br/>

## Step 3 - Add hosts to hostvars

You will be responsible for adding each device returned from the API call to the hostvars portion of the inventory.

You will have to use the JSON data contained in the `devices_json` variable to build the hostvars portion of the inventory. The `hostvars` variable has already been created for you, and it includes the basic structure needed.  

<br/>

* Each device's name should be a key in the `hostvars['_meta']['hostvars']` dictionary, and each one of these keys should have a value of a dictionary.

<br/>

* Within the dictionary for each respective device, set two host-level variables:

    * `ansible_host`
    * `device_type`

    You will have to set the value of these variables appropriately using the data returned from the API call.

    Write this code just beneath the `hostvars` variable.

<br/>

## Step 4 - Group hosts based on enclave

On line X, a `groups` variable has already been defined for you with the appropriate starting structure.  The `groups` variable is a dictionary that has 5 groups defined already:

* `all`
* `red_devices`
* `yellow_devices`
* `routers`
* `switches`

The problem is, each group has an empty `hosts` list.

Each device returned in the API call should have either `RED` or `YELLOW` in its name, indicating its enclave.  You will use this fact to put each device into either the `red_devices` or `yellow_devices` groups.

### Using a for-loop, loop through each device and add its hostname to the hosts list of either the `red_devices` or `yellow_devices` groups, depending on its name.

<br/>

## Step 5 - Group hosts based on role

Lastly, you need to add devices to the appropriate role-based groups based on whether they are a router or switch.

Every device hostname should have either `ROUTER` or `SWITCH` in it, indicated its device type.

### Within the SAME for-loop you used during the previous step, add the appropriate code to add each device's hostname to hosts list of either the `routers` or `switches` groups, depending on its name.

<br/>

## Step 6 - Add groups as children of the `all` group

Now, you need to make the `red_devices`, `yellow_devices`, `routers`, and `switches` groups _children_ of the `all` group.

### Using a NEW for-loop, add the `red_devices`, `yellow_devices`, `routers`, and `switches` groups names to the `groups['all']['children']` list.

<br/>

## Step 7 - Combine the inventory components into one variable

On line X, there is an `inventory` variable set to None.  

### Change the value of this variable to an empty dictionary.

### Then, update this dictionary with the `hostvars` and `groups` dictionaries.  

<br/>

## Step 8 - Print the inventory in JSON format

At the beginning of this script, the `json` module was already imported for you.  You will need to use a function within the `json` module to print out the entire inventory in a JSON formatted string.

### Using the `dumps()` function from the `json` module, print out the `inventory` variable in a JSON formatted string with an indentation level of `4`.

## Step 9 - Test your script

At this point, you will need to make sure you script works as intended.  

### Run your script within a Bash terminal on your lab VM.  The output should look like the following:

```json
{
    "all": {},
    "red_devices": {
        "hosts": [
            "PRACTICAL-RED-ROUTER",
            "PRACTICAL-RED-SWITCH"
        ]
    },
    "yellow_devices": {
        "hosts": [
            "PRACTICAL-YELLOW-ROUTER",
            "PRACTICAL-YELLOW-SWITCH"
        ]
    },
    "routers": {
        "hosts": [
            "PRACTICAL-RED-ROUTER",
            "PRACTICAL-YELLOW-ROUTER"
        ]
    },
    "switches": {
        "hosts": [
            "PRACTICAL-RED-SWITCH",
            "PRACTICAL-YELLOW-SWITCH"
        ]
    }
}
```

<br/>

## Step 10 - Make the script executable for all users

In a Bash terminal, execute the command that will make the script executable by _all users_.

<br/>

# Task 3 - Create the group variables

<br/>

## Step 1 - Create group-level variable files

Within the `playbooks` directory, there is already a `group_vars` directory created for you.  

Within `group_vars` directory, create a group-variables file for every group in the inventory **except the `all` group**.  These can be either JSON or YAML files.  

The `all` group should already have a JSON file with variables defined.

Within these files, define the following variables for each group:

* `red_devices`: 
    - A variable called `dns_servers` set to a list containing two IP addresses: `10.10.20.98` and `10.10.20.99`.

* `yellow_devices`: 
    - A variable called `dns_servers` set to a list containing two IP addresses: `10.10.30.98` and `10.10.30.99`.

* `routers`: 
    - A variable called `management_interface` set to `Loopback0`.

* `switches`:
    - A variable called `management_interface` set to `Vlan1000`.

<br/>

## Step 2 - Define connection variables for the `all` group

In the `all.json` file, define the `ansible_network_os`, `ansible_user`, and `ansible_ssh_pass` connection variables and give them the appropriate values:

* `ansible_network_os`: `ios`
* `ansible_user`: `orko`
* `ansible_ssh_pass`: `P@ssw0rd123!`

<br/>

# Task 4 - Complete the Jinja Templates

A `templates` directory has already been created for you within the `playbooks` directory.  There are a few partially completed Jinja templates that you will need to finish.

Throughout certain templates, you will see comments like this: `{# SOME COMMENT HERE #}`.  Each comment will have a step number correlating to the instructions in this README.

<br/>

## Step 1 - Configure the hostname

In `templates/base.j2`, fill in the empty variable call after `hostname` on the first line.

You will need to use the appropriate Ansible special variable.  

<br/>

## Step 2 - Import the required child templates

In `templates/base.j2`, use the comments provided to import the following child templates in the appropriate order:

* dns_servers.j2
* loopback_interfaces.j2
* management_interface.j2

<br/>

## Step 3 - Configure the logging host

At the end of the `base.j2` template, there is an empty variable call: `logging host {{ }}`. 

Fill in the empty variable call with a new variable name called `syslog_server`.  You will pass this variable as an extra variable later on when you run the playbook.

## Step 4 - Write the template for the dns server configuration

For this step, you will have to write the `dns_servers.j2` template to generate the dns server configuration for each device.

In this template, you will need to **loop** through the `dns_servers` variable to produce the Cisco-formatted DNS configuration.

The Jinja template should produce something like the following:

```
ip name-server <ip_address>
ip name-server <ip_address>
```

<br/>

## Step 5 - Write the template for the loopback interfaces configuration

For this step, you will need to finish the `loopback_interfaces.j2` template to generate the configuration for all physical interfaces.

Loop through the `interfaces` variable defined in the `all.json` group_vars file.

Create the appropriate cisco-formatted interface configuration using the data in the `interfaces` variable.

This template, once rendered, should produce output equal to the following:

```
interface Loopback50
  ip address 10.10.50.1 255.255.255.0
!
interface Loopback60
  ip address 10.10.60.1 255.255.255.0
!
interface Loopback70
 ip address 10.10.70.1 255.255.255.0
!
```

<br/>

# Task 5 - Write the Playbook

<br/>

## Step 1 - Create a playbook

* Within the `playbooks` directory, create a playbook called `build.yml`.

<br/>

## Step 2 - Create a play

Within your empty playbook, create a new play with a name of `Build Device Configuration`.

The play should:

* Not gather facts

* Target all hosts in the inventory

* Use a connection type of `network_cli`.  

<br/>

## Step 3 - Create a tasks list

Give your play a list of tasks.  **Every task should be accomplished by the localhost, and the name of each task does not matter.**

This list should define the following 6 tasks in this order:

1. Use the `set_fact` module to create a `start_time` variable, and set the value to the current system time.  **This task should be delegated to the localhost.**

2. Create a new directory to store device config files:

    * The directory name should be set to the `<start_time>-configs`.  For example: `20210101010101-configs`.

    * Use an Ansible special variable within the directory path to make sure the new directory is within the same directory as the playbook itself.

    * **This task should also be delegated to the localhost.**

3. Use the `template` module to generate device configuration files and store in the directory you created:

    * The `template` module should generate the `base.j2` template.

    * Each destination filename should contain the respective device's hostname and end with a `.cfg` file extension.  For example: `PRACTICAL-RED-ROUTER.cfg`.

    * Set an option for this task that tells the playbook to continue running even if the task fails.

4. Use the `ios_config` module to send the templated configs to the target devices:

    * The `ios_config` module should generate the `base.j2` template.


# Running the Playbook

- Run the playbook
    - Pass in an extra variable called syslog_server and set the value equal to 10.10.10.10


# Post-exam Steps
- Commit the changes to your branch

