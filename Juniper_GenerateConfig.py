#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

from jinja2 import FileSystemLoader, Environment
import yaml
import os

project_dir = "/media/bassim/DATA/GoogleDrive/work Flow-B/me-inside/CCIE-LAB/JuniperAutomation/"

with open(os.path.join(project_dir,"JuniperAutomation.yaml"), 'r') as isp_devices:
    isp_devices = yaml.load(isp_devices)  # This is to read the file content


router_env = Environment(
    loader=FileSystemLoader(project_dir),
    trim_blocks=True,
    lstrip_blocks= True
)

for router,router_config in isp_devices.iteritems():
    config_rendered = router_env.get_template("vMX_Template.j2").render(router_config)
    with open(os.path.join(project_dir, router + "_" + str(router_config['port']) + ".txt"), 'w') as config_file:
        config_file.write(config_rendered)
