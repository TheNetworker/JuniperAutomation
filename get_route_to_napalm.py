#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from napalm import get_network_driver
from prettytable import PrettyTable
import argparse

simplified_route = PrettyTable(['Route', 'Next Hop', 'Protocol', "Outgoing Interfaces"])
simplified_route.padding_width = 1


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--mx_ip", help="Enter the ip address")
parser.add_argument("-r", "--route", help="Enter the route")
args = parser.parse_args()
device_ip = args.mx_ip
route = args.route

junos_driver = get_network_driver("junos")

mx_router = junos_driver(username="root",
                         password="access123",
                         hostname=device_ip)
mx_router.open()
if mx_router.is_alive()["is_alive"]:
    print "working on device {}".format(device_ip)
    route_data = mx_router.get_route_to(route)
    try:
        simplified_route.add_row([route,route_data[route][0]["next_hop"],
                                  route_data[route][0]["protocol"],
                                  route_data[route][0]['outgoing_interface']])
    except Exception as e:
        print e

print simplified_route