import requests
import yaml
from datetime import datetime

# GNS3 Server configuration
GNS3_SERVER = "http://localhost:3080"
PROJECT_ID = "<INSERT_YOUR_PROJECT_ID_HERE>"  # Replace with your actual project UUID

# Nodes of interest (manually specify the hostnames of the Windows desktops and test boxes)
TARGET_NODE_NAMES = [
    "Windows_Desktop_1",
    "Windows_Desktop_2",
    "Windows_Desktop_3",
    "Windows_Desktop_4",
    "TestBox_1",
    "TestBox_2"
]

def fetch_nodes():
    url = f"{GNS3_SERVER}/v2/projects/{PROJECT_ID}/nodes"
    response = requests.get(url)
    return response.json()

def get_inventory_for_nodes(nodes):
    inventory = {"hosts": {}}
    for node in nodes:
        name = node["name"]
        if name in TARGET_NODE_NAMES:
            general = {
                "name": name,
                "RAM": node["properties"]["ram"],
                "vCPUs": node["properties"]["cpus"],
                "QEMU_binary": node["properties"]["qemu_path"],
                "boot_priority": node["properties"]["boot_priority"],
                "on_close": node["properties"]["on_close"],
                "console_type": node["console_type"]
            }

            network = {
                "adapters": node["properties"]["adapters"],
                "mac_address": node["properties"]["mac_address"],
                "nic_type": node["properties"]["adapter_type"],
                "replicate_state": node["properties"]["replicate_network_connection_state"]
            }

            inventory["hosts"][name] = {
                "general_settings": general,
                "network_settings": network
            }
    return inventory

def save_inventory_to_yaml(inventory, filename):
    with open(filename, "w") as file:
        yaml.dump(inventory, file, sort_keys=False)

def main():
    nodes = fetch_nodes()
    inventory = get_inventory_for_nodes(nodes)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"host_inventory_{timestamp}.yaml"
    save_inventory_to_yaml(inventory, filename)
    print(f"Inventory saved to: {filename}")
    print("--- Inventory Preview ---")
    print(yaml.dump(inventory, sort_keys=False))

if __name__ == "__main__":
    main()