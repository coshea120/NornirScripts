from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
import getpass
from yaml import safe_load

output_path = "C:\\users\\osheac\\Documents\\show command output\\"

username = getpass.getuser()
password = getpass.win_getpass(f"Enter password for {username}:")

nr = InitNornir(config_file="config.yaml")
nr.inventory.defaults.username = username
nr.inventory.defaults.password = password

with safe_load("show_commands.yaml") as commands_handle:
    for vdc, command_list in commands_handle.items():
        for command in command_list:
            result = nr.run(netmiko_send_command, command_string=command)
            with open(f"{output_path}{command.replace('|','')}.txt", 'w') as output_handle:
                output_handle.write(result)



