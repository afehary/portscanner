#!/usr/bin/env python3
from portscanner import get_input, is_port_open
import socket

def services(ip_addresses, ports):
    for ip in ip_addresses:
        for port in ports:
            is_open, banner = is_port_open(ip, port, grab_banner=True)  # Pass grab_banner=True to get version info
            if is_open:
                try:
                    # Get the standard service name
                    service = socket.getservbyport(port)
                    print(f"IP: {ip}, Port {port}, Service: {service}")

                    if banner:
                        print(f"Service Version on Port {port}: {banner}")
                    else:
                        print(f"Could not determine service version for Port {port}")
                except OSError:
                    print(f"IP: {ip}, Port {port}, Service: Unknown")
            else:
                continue

def main():
    ips, ports = get_input()  # Reuse input and validation logic from portscanner.py
    if ips and ports:
        services(ips, ports)

if __name__ == "__main__":
    main()
