import os
import subprocess
import sys
import logging
from datetime import datetime

# Author: MR.Gh0st
# Position: Hacker
# Date: 2024-10-22
# Time: 14:45

LOG_FILE = '/var/log/port_configurator.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_root():
    if os.geteuid() != 0:
        sys.exit("Please run this script as root.")

def log_info(message):
    logging.info(message)
    print(f"[INFO] {message}")

def log_error(message):
    logging.error(message)
    print(f"[ERROR] {message}")

def validate_port(port):
    if not port.isdigit():
        return False
    port_num = int(port)
    return 1 <= port_num <= 65535

def add_firewall_rule(port, protocol='tcp'):
    try:
        subprocess.run(["ufw", "allow", f"{port}/{protocol}"], check=True)
        subprocess.run(["ufw", "allow", f"v6:{port}/{protocol}"], check=True)
        log_info(f"Firewall rule added for {port}/{protocol} (IPv4 & IPv6)")
    except subprocess.CalledProcessError as e:
        log_error(f"Failed to add firewall rule for port {port}: {e}")

def configure_listener_service(port, protocol='tcp'):
    service_file = f"/etc/systemd/system/listen_on_port_{port}.service"
    service_content = f"""
[Unit]
Description=Listener on {protocol.upper()} Port {port}
After=network.target

[Service]
ExecStart=/usr/bin/nc -l -p {port} -k -v
Restart=always
User=nobody
Group=nogroup

[Install]
WantedBy=multi-user.target
"""
    try:
        with open(service_file, 'w') as f:
            f.write(service_content)
        log_info(f"Created systemd service for port {port} at {service_file}")

        subprocess.run(["systemctl", "daemon-reload"], check=True)
        subprocess.run(["systemctl", "start", f"listen_on_port_{port}.service"], check=True)
        subprocess.run(["systemctl", "enable", f"listen_on_port_{port}.service"], check=True)
        log_info(f"Service listen_on_port_{port} started and enabled.")
    except Exception as e:
        log_error(f"Failed to create systemd service for port {port}: {e}")

def add_ports(ports, protocol='tcp'):
    for port in ports:
        if validate_port(port):
            add_firewall_rule(port, protocol)
            configure_listener_service(port, protocol)
        else:
            log_error(f"Invalid port: {port}. Skipping configuration.")

def main():
    check_root()

    ports_input = input("Enter the ports to allow and listen on (comma-separated, e.g., 8080,6320,1234): ")
    protocol_input = input("Enter the protocol (tcp/udp) [default: tcp]: ") or "tcp"

    if protocol_input.lower() not in ['tcp', 'udp']:
        log_error("Invalid protocol. Only 'tcp' or 'udp' are allowed.")
        sys.exit(1)

    ports = [port.strip() for port in ports_input.split(",")]

    add_ports(ports, protocol_input.lower())

    log_info("\nConfiguration complete. The specified ports are now open and listening.")
    print(f"Check log file for details: {LOG_FILE}")

if __name__ == "__main__":
    main()
