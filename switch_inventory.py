from datetime import datetime

# Switch config data (edit to match your actual values from GNS3)
switches = {
    "local_switch": {
        "ansible_host": "10.10.1.24",
        "general": ["Local_Switch", "512Mb", "1", "/usr/bin/qemu-system-x86_64 (v4.2.1)", "CD/DVD-ROM or HDD", "Power off the VM", "telnet"],
        "network": ["13", "0c:c0:5e:66:00:00", "Realtek 8139 Ethernet (rtl8139)", "true"]
    },
    "user_network": {
        "ansible_host": "10.10.1.22",
        "general": ["User_Network", "512Mb", "1", "/usr/bin/qemu-system-x86_64 (v4.2.1)", "CD/DVD-ROM or HDD", "Power off the VM", "telnet"],
        "network": ["13", "0c:e0:f2:0b:00:00", "Realtek 8139 Ethernet (rtl8139)", "true"]
    },
    "acct_network": {
        "ansible_host": "10.10.1.32",
        "general": ["ACCT_Network", "512Mb", "1", "/usr/bin/qemu-system-x86_64 (v4.2.1)", "CD/DVD-ROM or HDD", "Power off the VM", "telnet"],
        "network": ["13", "0c:40:34:07:00:00", "Realtek 8139 Ethernet (rtl8139)", "true"]
    },
    "mgmt_network": {
        "ansible_host": "10.10.1.31",
        "general": ["MGMT_Network", "512Mb", "1", "/usr/bin/qemu-system-x86_64 (v4.2.1)", "CD/DVD-ROM or HDD", "Power off the VM", "telnet"],
        "network": ["13", "0c:cc:78:5d:00:00", "Realtek 8139 Ethernet (rtl8139)", "true"]
    },
    "it_network": {
        "ansible_host": "10.10.1.30",
        "general": ["IT_Network", "512Mb", "1", "/usr/bin/qemu-system-x86_64 (v4.2.1)", "CD/DVD-ROM or HDD", "Power off the VM", "telnet"],
        "network": ["13", "0c:1c:b2:85:00:00", "Realtek 8139 Ethernet (rtl8139)", "true"]
    }
}

# Output file
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"switch_inventory_{timestamp}.ini"

# Write to file
with open(output_file, "w") as f:
    f.write("[switches]\n")
    for name, data in switches.items():
        f.write(f"{name} general_settings={','.join(data['general'])}\n")
        f.write(f"{name} network_settings={','.join(data['network'])}\n")
        f.write(f"{name} ansible_host={data['ansible_host']}\n")
    f.write("\n[switches:vars]\n")
    f.write("ansible_user=ssh_user\n")
    f.write("ansible_ssh_pass=P@ssw0rd\n")
    f.write("ansible_connection=network_cli\n")
    f.write("ansible_network_os=exos\n")

print(f"Inventory saved to: {output_file}")