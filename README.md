# mod_3_practical

## Topics to cover:
- python
- api calls
- yaml/json
- ansible

# Build device configuration files with Ansible

# Task 1 - Preparation

## Step 1 - Set up Remote-SSH

* Use Git Bash to send your windows laptops SSH public key to your lab VM.  
* Use the Remote-SSH extension in VS Code to open a session to your lab VM.

## Step 2 - Clone the practical exam repository

* On your lab VM, generate an SSH key-pair.
* Add the new public key to your profile in Gitlab.
* Clone the exam repo to your lab VM using SSH and go into the top-level directory of the repo.
* Create a new branch from the _development_ branch, and name it `StudX-Practical`, where `X` is your personal student number.

# Task 1 - Finish the `partial_inventory.py` dynamic inventory script

Each of the following steps will have you either complete a section or create code from scratch in the `partial_inventory.py` in the `ansible` directory.  Each of the following steps will correlate to an appropriately labeled comment within the script so that you will know what the directions are referencing.

## Step 1 - Build API call variables

This script will execute an API call to the locally hosted Nautobot server.  The API call was intended to _retrieve_ the information for all devices that belong to the site `orko_mod_3_practical`.  You will need to fix the API call variables.

* Login to the local Nautobot server at `https://10.10.44.21`.  There is already an account set up for you.  The username is `studX`, where `X` is your personal student number, and the password is `P@ssw0rd123!`.

* Once logged in, open your account profile, and find your personal API token.  You will need it for the script.

* Lines 10-14 will need to be completed by setting the constants to their appropriate values, excluding the `DEVICES_API_URL` constant which has already been defined for you.  You will need to set the values for these variables:

    * `NAUTOBOT_TOKEN`
    * `DEVICES_API_URL`
    * `METHOD`
    * `HEADERS`
    * `PARAMETERS`

* The `NAUTOBOT_TOKEN` variable needs to be set to a string containing your personal API token.

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

## Step 3 - Add hosts to hostvars

* Use the JSON data in the `devices_json` variable to build the hostvars portion of the inventory. The `hostvars` variable has already been created for you, and it includes the basic structure needed.  

    ### If you'd like, you can test this API call in Thunderclient to make sure it works before attempting to run this script.

You will be responsible for adding each device returned from the API call to the hostvars.

Additionally, each host should have two host-level variables:

* `ansible_host`
* `device_type`

You will have to set the value of these variables appropriately using the data returned from the API call.

Write your code just beneath the `hostvars` variable.

## Step 4 - Group hosts based on enclave

The word 'red' or 'yellow' will be in each device's hostname.  This will indicate the enclave of the device. 

Use this to put all the 'red' devices into the 'red_devices' group, and all the 'yellow' devices into the 'yellow_devices' group.

Put this code after the code you wrote for the previous step.

## Step 5 - Group hosts based on role

Lastly, add devices to the appropriate role-based groups based on whether they are a router or switch.

Every device hostname should have either 'router' or 'switch' in it. Use this to put each device into either the 'routers' group or the 'switches' group.

## Step 6 - Add groups as children of the 'all' group

Edit the all group so that it will contain the other 4 groups as nested groups.

## Step 7 - Combine the inventory components into one variable

There is an `inventory` variable set to None.  Change the value of this variable and use whatever code you need to in order to combine the `hostvars` and `groups` variables into a single object.

## Step 8 - Print the inventory in JSON format

Lastly, use the approriate code to print the inventory in a JSON format.  This step will include adding an additional import statement to the beginning of the script.

## Step 9 - Make the script executable

In a bash terminal, execute the command that will make the script executable by all users, including the Ansible user.

## Step 10 - Test the script

In a bash terminal, navigate to the same directory as the partial inventory script, and use the appropriate Ansible command to print a graph of the group structure of the inventory. You should get the following output:

```
@all:
  |--@red_devices:
  |  |--orko-mod3-practical-red-router
  |  |--orko-mod3-practical-red-switch
  |--@routers:
  |  |--orko-mod3-practical-red-router
  |  |--orko-mod3-practical-yellow-router
  |--@switches:
  |  |--orko-mod3-practical-red-switch
  |  |--orko-mod3-practical-yellow-switch
  |--@ungrouped:
  |--@yellow_devices:
  |  |--orko-mod3-practical-yellow-router
  |  |--orko-mod3-practical-yellow-switch
```
If you do not see this output, you have done something wrong.

# Task 2 - Create the group variables

## Step 1 - Create group-level variable files

Within the appropriate directory for group-level variable files, create a file for every group in the inventory _except the all group_.  These can be either JSON or YAML files.  The all group should already have a JSON file.

Within these files, create the following variables for each group:

* red_devices: 
    - A variable called `dns_servers` set to a list containing two IP addresses: 10.10.20.98 and 10.10.20.99.

* yellow_devices: 
    - A variable called `dns_servers` set to a list containing two IP addresses: 10.10.30.98 and 10.10.30.99.

* routers: 
    - A variable called `management_interface` set to `Loopback0`.

* switches:
    - A variable called `management_interface` set to `Vlan1000`.


# Task 3 - Complete the Jinja Templates


## Step 1 - Configure the hostname

In `templates/base.j2`, fill in the empty variable call after 'hostname' on the first line using an ansible special variable.  This special variable should be the hostname for any given device.

## Step 2 - Import the required child templates

In `templates/base.j2`, use the comments provided to import the following child templates in the appropriate places:

* dns_servers.j2
* physical_interfaces.j2
* management_interface.j2


## Step 3 - Write the template for the physical interface configuration

Finish the 'physical_interfaces.j2' template to generate the configuration for all physical interfaces.

Loop through the `interfaces` variable defined in the 'all.json' group_vars file.

Create the appropriate cisco-formatted interface configuration using the data in the `interfaces` variable.

This template, once rendered, should product output equal to the following:

```
interface Gi2
  ip address 10.10.50.1 255.255.255.0
!
interface Gi3
  ip address 10.10.60.1 255.255.255.0
!
interface Gi4
 ip address 10.10.70.1 255.255.255.0
!
```

## Step 4 - Write the template for the dns server configuration

Write the 'dns_servers.j2' template to generate the dns server configuration.

Loop through the `dns_servers` variable to produce the Cisco-formatted DNS configuration.

The Jinja template should produce the following:

```
ip name-server <ip_address>
ip name-server <ip_address>
```

## Step 5 - Write the template to configure the management interface

Finish the 'management_interface.j2' template.

Fill in the empty variable calls with the appropriate variables:

* The management interface's IP address should be the primary IP address of the host
* Use a ternary variable assignment to determine the subnet mask
* It should be `255.255.255.255` if the device_type is `router`, else set it to `255.255.255.0`

# Task 4 - Write the Playbook


## Step 1 - Create a playbook

Within the appropriate directory, create a playbook called 'build.yml'.

## Step 2 - Create a play

Within your empty playbook, create a new play with a name of `Build Device Configuration`.

The play should not gather facts, it should target all hosts in the inventory, and it should use a connection type of `network_cli`.  

## Step 3 - Create a tasks list

Give your play a list of tasks.  Every task should be accomplished by the localhost.

The playbook should have 6 tasks:

1. Create the `start_time` variable and set the value to the current system time.
2. Create a directory to store device config files.
    * Make sure the new directory is a sub-directory of the playbooks directory.
    * Use the `start_time` variable in the name of the new directory. For example: `playbooks/20210101010101-configs/`.
3. Generate device configuration files and store in the directory you created.
    * Output the files in a .cfg format.
    * Each device's config file should have it's hostname in the name of the file.
    * Set the playbook to continue if the config generation fails for any one device.
6. Send the new config files to the appropriate devices so that when they restart, the new configuration would take effect.
7. Send a command to each device telling it to restart.


# Running the Playbook

- Run the playbook
    - Pass in an extra variable called syslog_server and set the value equal to 10.10.10.10


# Post-exam Steps
- Commit the changes to your branch

