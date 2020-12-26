#!/usr/bin/env python

from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

nornir_instance = InitNornir(config='config.yaml')
