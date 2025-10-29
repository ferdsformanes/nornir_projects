from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command



# Initialize Nornir with config.yaml
nr = InitNornir(config_file="config.yaml")
host = nr.inventory.hosts["switch1"]
print(host.keys)
# Run a simple command
result = nr.run(
    task=netmiko_send_command,
    command_string="show ip bgp summary"
)
# Print results
for host, multi_result in result.items():
    print(f"\n--- {host} ---")
    print(multi_result[0].result)
