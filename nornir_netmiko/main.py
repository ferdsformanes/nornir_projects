from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

# Initialize Nornir
nr = InitNornir(config_file="config.yaml")

# Run 'show version' on all hosts
result = nr.run(task=netmiko_send_command, command_string="show version")

# Print the results
print_result(result)