from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

# Initialize Nornir
nr = InitNornir(config_file="config.yaml")

# Run NAPALM 'get_facts' on all hosts
result = nr.run(task=napalm_get, getters=["get_facts"])

# Print the results
print_result(result)