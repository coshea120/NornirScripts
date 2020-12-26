#!/usr/bin/env python

from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command, netmiko_send_config
from nornir.plugins.functions.text import print_result, print_title

nr = InitNornir(config="config.yaml", dry_run=True)
result = nornir.run(netmiko_send_command, command_string="ntp server " + nr.defaults['ntp_server'])
print_result(result)
