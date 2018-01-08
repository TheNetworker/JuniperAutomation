#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from napalm import get_network_driver
from pprint import pprint
from datetime import datetime

devices_ip = ["10.131.71.10",
              "10.131.71.20",
              "10.131.71.30",
              "10.131.71.40",
              "10.131.71.60",
              "10.131.71.100",
              "10.131.71.200",
              "10.131.71.250",
              ]

for ip in devices_ip:
    junos_driver = get_network_driver("junos")

    mx_router = junos_driver(hostname=ip,
                             username="root",
                             password="access123")

    mx_router.open()

    if mx_router.is_alive()["is_alive"]:
        print str(datetime.now()) + " Getting Data from {}" .format(ip)
    pprint(mx_router.get_facts())
    print "=" * 80
else:
    print "Device {} is unrechable, cannot execute command" .format(ip)