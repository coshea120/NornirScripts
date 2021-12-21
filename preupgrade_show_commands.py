#!/usr/bin/env python

from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
import getpass
from yaml import safe_load

output_path = "C:\\users\\osheac\\Documents\\show command output\\"

####################################################################################################
#
# Name: run_show_command_list
#
# Description: This function runs a list of show commands on a target device via Nornir.  Also
#              supports switching to agg and otv vdc's for core switches.  Defaults to admin vdc.
#              Output is written to a file named after the show command that was run.
#
# Parameters: command_list - list of strings representing the list of show commands to run
#             nornir_instance - nornir object to send commands and receive output.  Assumes object
#             has already been instantiated.
#             vdc - string representing which vdc the show commands will run on.
#
# Return Value: None
####################################################################################################


def run_show_command_list(command_list, nornir_instance, vdc="admin_vdc"):

    nornir_instance.run(netmiko_send_command, command_string="terminal length 0")
    for command in command_list:
        result = nornir_instance.run(netmiko_send_command, command_string=command)

        for hostname in result:
            if vdc == "admin_vdc":
                filename = f"{output_path}{hostname}-{command.replace('|', '')}.txt"
            else:
                filename = f"{output_path}{hostname}-{vdc}-{command.replace('|', '')}.txt"

            with open(filename, 'w') as output_handle:
                output_handle.write(result[hostname][0].result)


#########################################################################################################
# __main__ entry point
#########################################################################################################


if __name__ == '__main__':
    username = getpass.getuser()
    password = getpass.win_getpass(f"Enter password for {username}:")

    nr = InitNornir(config_file="config.yaml")
    nr.inventory.defaults.username = username
    nr.inventory.defaults.password = password

    with open("show_commands.yaml", "r") as commands_handle:
        show_commands_yaml = safe_load(commands_handle)

    for (hostname, host) in nr.inventory.hosts.items():
        if "VDCs" in host.keys():
            if 'agg' in host["VDCs"]:
                nr.run(netmiko_send_command, command_string="switchto vdc agg", expect_string=r'#')
                run_show_command_list(show_commands_yaml["agg_vdc"], nr, vdc='agg_vdc')
                nr.run(netmiko_send_command, command_string="switchback", expect_string=r'#')

            if 'otv' in host["VDCs"]:
                nr.run(netmiko_send_command, command_string="switchto vdc otv", expect_string=r'#')
                run_show_command_list(show_commands_yaml["otv_vdc"], nr, vdc='otv_vdc')
                nr.run(netmiko_send_command, command_string="switchback", expect_string=r'#')

        run_show_command_list(show_commands_yaml["admin_vdc"], nr)



