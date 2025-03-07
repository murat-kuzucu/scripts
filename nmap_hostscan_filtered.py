"""
nmap -sn -PE 192.168.1.0/24 >> hosts.txt
python3 nmap_hostscan_filtered.py hosts.txt
"""

import re

def extract_host_ips(nmap_output):
    # Regular expression to match IP addresses in Nmap scan reports
    ip_pattern = re.compile(r'Nmap scan report for (?:[\w.-]+ )?\(?([\d.]+)\)?')
    
    # Extract all matching IPs
    host_ips = ip_pattern.findall(nmap_output)
    
    return host_ips

# Read Nmap output from hosts.txt
with open("hosts.txt", "r") as file:
    nmap_output = file.read()

# Extract and print host IPs
host_ips = extract_host_ips(nmap_output)

# Save extracted IPs to a file
with open("extracted_hosts.txt", "w") as file:
    file.write("\n".join(host_ips))

print("Filtered Host IPs saved to extracted_hosts.txt")
