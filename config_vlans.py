#!/usr/bin/env python

from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result
import getpass

username = getpass.getuser()
password = getpass.win_getpass(f"Enter password for {username}:")
nr = InitNornir(config_file="config.yaml")
nr.inventory.defaults.username = username
nr.inventory.defaults.password = password

