# VLAN Deployment Process – Section D

This document outlines the process used to complete the VLAN deployment in Parts A, B, and C of the D417 Performance Assessment. The description includes validation, testing, and troubleshooting.

---

## Part A – Python Library Validation

To begin, I ran `pip list` on the Ansible control node to verify that all required libraries were installed. These included:

- `netmiko`
- `pyyaml`
- `paramiko`
- and other standard Python packages used for automation


A screenshot of the terminal output was taken to document the installed libraries and confirm readiness for automation tasks.

---

## Part B – Inventory File Creation

A Python script named `switch_inventory.py` was created to extract device configuration details for each switch in Access Closet 1 on the 10.10.1.1 network.

The script pulled information from the GNS3 API and generated a structured YAML file with the following:

- **General Settings**: Name, RAM, vCPUs, QEMU binary, boot priority, power-off behavior, and console type
- **Network Settings**: Adapter count, base MAC address, NIC type, and replicate state

The resulting YAML file was validated by visually comparing its content with the information displayed in the GNS3 device configuration tabs. Screenshots were taken for submission.

---

## Part C – VLAN Configuration and Git Integration

### 1. VLAN Identification Script

A Python script using Netmiko was written to connect to each EXOS switch and run the `show vlan` command. The script confirmed existing VLANs on each switch and printed the results to the terminal.

### 2. VLAN Deployment Script

Another script was created to configure the required VLANs per the scenario. This included defining VLAN IDs and names and applying them across the Access Closet 1 switches. Execution was validated by rerunning the identification script and observing the newly created VLANs.

### 3. Verification of VLAN Configuration

Successful VLAN deployment was verified by:

- Viewing the updated VLAN list from each switch
- Capturing screenshots showing the VLANs present on each device
- Comparing script output with expected configuration

### 4. GitLab Repository for CI

All scripts and supporting files were committed to a **private GitLab repository** named:

```
004862484_D417_1
```

The `WGU-Evaluation` account was added as a member with Reporter access. Screenshots and the repository URL were included for validation.

---

## Validation

Validation was performed at each step by confirming that:

- Required libraries were installed (`pip list`)
- Inventory output matched device configuration in GNS3
- VLANs were properly displayed before and after deployment
- Git commits and push actions reflected current progress

---

## Testing

Scripts were executed sequentially to ensure:

- Network access to all switches was working
- Inventory and VLAN scripts produced accurate, readable output
- VLAN changes were applied only once and persisted between runs

All scripts included print statements and logging to aid in quick testing and confirmation.

---

## Troubleshooting

Issues encountered and resolved included:

- **SSH Failures**: Resolved by enabling Telnet/SSH on each EXOS switch manually
- **Incorrect IPs**: Inventory was updated to reflect actual switch IPs in the 10.10.1.x range
- **YAML Formatting Errors**: Fixed spacing and structure for compatibility with Ansible
- **GitLab SSH Key Issues**: Resolved by generating a new SSH key, uploading it to GitLab, and testing with `ssh -T git@gitlab.com`

---

All steps and fixes were documented and version-controlled for full transparency and repeatability.