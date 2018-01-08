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
        try:
            pprint(mx_router.compliance_report("/root/napalm_scripts/check_health.yaml"))
            print "\n" * 6
        except Exception as e:
            print "unable to validate host {} " .format(ip)
            print e

