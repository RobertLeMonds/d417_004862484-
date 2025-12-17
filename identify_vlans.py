# identify_vlans.py

from netmiko import ConnectHandler
from datetime import datetime

# Define switches in Access Closet 1
switches = [
    {
        "name": "local_switch",
        "host": "10.10.1.24"
    },
    {
        "name": "user_network",
        "host": "10.10.1.22"
    },
    {
        "name": "acct_network",
        "host": "10.10.1.32"
    },
    {
        "name": "mgmt_network",
        "host": "10.10.1.31"
    },
    {
        "name": "it_network",
        "host": "10.10.1.30"
    }
]

username = "ssh_user"
password = "P@ssw0rd"
device_type = "extreme_exos"
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"vlan_output_{timestamp}.txt"

with open(output_file, "w") as log:
    log.write(f"VLAN Discovery Log - {timestamp}\n\n")

    for sw in switches:
        print(f"Connecting to {sw['name']} ({sw['host']})...")
        try:
            connection = ConnectHandler(
                device_type=device_type,
                host=sw["host"],
                username=username,
                password=password
            )
            output = connection.send_command("show vlan")

            print(f"\n=== VLANs on {sw['name']} ===\n{output}\n")

            log.write(f"=== VLANs on {sw['name']} ({sw['host']}) ===\n")
            log.write(output + "\n\n")

            connection.disconnect()

        except Exception as e:
            print(f"Failed to connect to {sw['name']}: {e}")
            log.write(f"[ERROR] {sw['name']} - {e}\n\n")

print(f"\nScript complete. Output saved to: {output_file}")