#!/usr/bin/python

"""
Converts encoded values in F5 BIG-IP cookie to decoded IP address and TCP port values.

Example usage: python3 bigip_cookie_decode.py BIGipServer<pool_name>=1677787402.36895.0000
"""

import sys
import struct

# Print usage and exit if no cookie is provided
if len(sys.argv) != 2:
    print(f"[-] Usage: {sys.argv[0]} cookie")
    sys.exit()

# Store and print cookie to decode
cookie = sys.argv[1]
print(f"\n[*] Cookie to decode: {cookie}\n")

# Try/Except to gracefully handle errors
try:
    # Split cookie value from BIG-IP prefix
    cookie = cookie.split("BIGipServer")[1]

    # Split cookie name and encoded data
    cookie_name, cookie_value = cookie.split('=')

    # Get encoded host and port fields. Discard third field
    host, port, _ = cookie_value.split('.')

    # Construct IP address from encoded host field
    ip = ".".join([str(i) for i in struct.pack("<I", int(host))])

    # Construct TCP port from encoded port field
    port_hex = list(struct.pack("<H", int(port)))
    port = int(f"0x{port_hex[0]:x}{port_hex[1]:x}", 16)

    # Output pool name and decoded ip/port
    print(f"[*] Pool name: {cookie_name}")
    print(f"[*] Decoded IP and Port: {ip}:{port}")
except Exception as e:
    # Print error details if one occurs, then exit
    print(f"[-] An error occurred while processing cookie: {e}")
    print("[-] Check cookie formatting.")
    sys.exit(1)
