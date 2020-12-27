#!/usr/bin/env python

from nornir import InitNornir
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result, print_title

nr = InitNornir(config="config.yaml", dry_run=True)
snmp_config = nr.defaults['snmp']
result = nr.run(netmiko_send_command, command_string="snmp community " + snmp_config['comm_str'])
print_result(result)
