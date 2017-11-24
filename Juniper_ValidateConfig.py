#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from netmiko import ConnectHandler
import re

import yaml
import os

project_dir = "/root/"

with open(os.path.join(project_dir,"JuniperAutomation.yaml"), 'r') as isp_devices:
    isp_devices = yaml.load(isp_devices)  # This is to read the file content


for router,router_config in isp_devices.iteritems():

    Device = {"device_type": "juniper",
                   "ip": router_config['mgmt_ip'],
                   "port": 22,
                   "username": "root",
                   "password": "access123",
                   # 'verbose': True,
                   'timeout': 30,
                   }

    try:
        net_connect = ConnectHandler(**Device)

        BGP_Output = net_connect.send_command("show bgp summary")

        #Check BGP Neighbors

        BGP_Neighbors_In_Prod = re.findall( r'\d+\.\d+\.\d+\.\d+', BGP_Output)

        BGP_Neighbors_In_Config = router_config['bgp']['neighbors'].keys()

        if sorted(BGP_Neighbors_In_Config) == sorted(BGP_Neighbors_In_Prod):
            print "***** BGP Neighbors in Router {} are configured correctly *****" .format(router)

        else:
            print "***** BGP Neighbors in Router {} *IS NOT* configured correctly *****" .format(router)
    except:
        pass
