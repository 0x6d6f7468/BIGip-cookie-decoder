#!/usr/bin/python

# example string: BIGipServer<pool_name>=1677787402.36895.0000

import sys
import struct

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} cookie")
    sys.exit()

cookie = sys.argv[1]
print(f"\n[*] Cookie to decode: {cookie}\n")

cookie = cookie.split("BIGipServer")[1]
cookie_name, cookie_value = cookie.split('=')

host, port, _ = cookie_value.split('.')

ip = ".".join([str(i) for i in struct.pack("<I", int(host))])

port_hex = list(struct.pack("<H", int(port)))
port = int(f"0x{port_hex[0]:x}{port_hex[1]:x}", 16)

print(f"[*] Pool name: {cookie_name}")
print(f"[*] Decoded IP and Port: {ip}:{port}")
