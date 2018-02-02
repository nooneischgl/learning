#!/usr/bin/env python3
import socket

def print_machine_info():
    """Print host_name and IP address"""
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print("Host Name: %s" %host_name)
    print("IP Address: %s" %ip_address)

if __name__ == '__main__':
    print_machine_info()