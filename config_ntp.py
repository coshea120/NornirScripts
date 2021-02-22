#!/usr/bin/env python

from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config="config.yaml")
result = nr.run(netmiko_send_command, command_string="ntp server " + nr.defaults['ntp_server'])
print_result(result)
