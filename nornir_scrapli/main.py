from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

# Initialize Nornir
nr = InitNornir(config_file="config.yaml")

# Run 'show version' on all hosts using Scrapli
result = nr.run(task=send_command, command="show version")

# Print the results
print_result(result)