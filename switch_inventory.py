import json
from datetime import datetime

# Manually entered GNS3 values from the right-click -> Configure screen
switch_inventory = {
    "name": "Local_Switch",
    "general_settings": {
        "RAM": "512 MB",
        "vCPUs": "1",
        "QEMU binary": "/usr/bin/qemu-system-x86_64",
        "Boot Priority": "CD/DVD first",
        "On close": "power_off",
        "Console type": "telnet"
    },
    "network_settings": {
        "Adapters": 6,
        "Base MAC": "00:1C:0D:AA:BB:01",
        "Type": "qemu",
        "Replicate connection state": True
    }
}

# Save with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"switch_inventory_output_{timestamp}.json"

with open(filename, "w") as f:
    json.dump(switch_inventory, f, indent=2)

print(f"Inventory exported to: {filename}")
