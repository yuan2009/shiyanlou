#!/usr/bin/env python3
from socket import socket
import sys

path = sys.path[0]
port_file = path + '/ports'
host_file = path + '/hosts.tmp'
# host = '127.0.0.1'
# port = 80
port_list = []
# with open(port_file) as f:
#     port_list.append(f.readlines())
# print(port_list)
f = open(port_file, 'r')
for port in f.readlines():
    port_list.append(port)

# print(port_list)
def scan(host, port):
    s = socket()
    s.settimeout(1)
    host = host
    port = int(port)
    if s.connect_ex((host, port)) == 0:
        print(host, port, ' open')
    else:
        # print(host, port, ' \033[31m close \033[0m')
        pass
if __name__ == '__main__':
    f = open(host_file, 'r')
    for list in f.readlines():
        host = list.split()[0]
        # port = list.split()[1]
        for port in port_list:
            scan(host, port)


