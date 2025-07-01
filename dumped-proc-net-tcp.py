import socket
import struct

def hex_to_ip(hex_str):
    return socket.inet_ntoa(struct.pack("<I", int(hex_str, 16)))

def hex_to_port(hex_str):
    return int(hex_str, 16)

def parse_tcp_line(line):
    parts = line.strip().split()
    if len(parts) < 4:
        return None
    
    local_addr = parts[1].split(':')
    remote_addr = parts[2].split(':')
    
    local_ip = hex_to_ip(local_addr[0])
    local_port = hex_to_port(local_addr[1])
    remote_ip = hex_to_ip(remote_addr[0])
    remote_port = hex_to_port(remote_addr[1])
    
    return f"{local_ip}:{local_port} -> {remote_ip}:{remote_port} [{parts[3]}]"

data = input("Paste dumped /proc/net/tcp data: ")
lines = data.strip().split('\n')[1:]
for line in lines:
    result = parse_tcp_line(line)
    if result:
        print(result)
