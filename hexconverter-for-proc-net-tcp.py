import socket
import struct

def hex_to_ip(hex_str):
    return socket.inet_ntoa(struct.pack("<I", int(hex_str, 16)))

def hex_to_port(hex_str):
    return int(hex_str, 16)

hex_input = input("Enter hex: ")
ip = hex_to_ip(hex_input)
print(ip)