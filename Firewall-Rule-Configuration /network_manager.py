#!/usr/bin/env python3
import os
import subprocess
import sys
import logging

# Author: MR.Gh0st
# Position: Hacker
# Date: 2024-10-22
# Time: 16:00

LOG_FILE = '/var/log/network_manager.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    logging.info(message)
    print(f"[INFO] {message}")

def log_error(message):
    logging.error(message)
    print(f"[ERROR] {message}")

def get_network_interfaces():
    try:
        interfaces = subprocess.check_output(["ip", "link", "show"]).decode().strip()
        log_info("Fetched network interfaces.")
        return interfaces
    except subprocess.CalledProcessError as e:
        log_error(f"Error fetching network interfaces: {e}")
        sys.exit(1)

def list_ip_addresses(interface):
    try:
        ip_addresses = subprocess.check_output(["ip", "addr", "show", interface]).decode().strip()
        log_info(f"IP addresses for {interface}: {ip_addresses}")
        return ip_addresses
    except subprocess.CalledProcessError as e:
        log_error(f"Error fetching IP addresses for {interface}: {e}")
        return ""

def add_ip_address(interface, ip, subnet):
    try:
        subprocess.run(["ip", "addr", "add", f"{ip}/{subnet}", "dev", interface], check=True)
        log_info(f"Added IP {ip}/{subnet} to {interface}.")
    except subprocess.CalledProcessError as e:
        log_error(f"Error adding IP address {ip} to {interface}: {e}")

def delete_ip_address(interface, ip, subnet):
    try:
        subprocess.run(["ip", "addr", "del", f"{ip}/{subnet}", "dev", interface], check=True)
        log_info(f"Deleted IP {ip}/{subnet} from {interface}.")
    except subprocess.CalledProcessError as e:
        log_error(f"Error deleting IP address {ip} from {interface}: {e}")

def configure_gateway(gateway):
    try:
        subprocess.run(["ip", "route", "add", f"default via {gateway}"], check=True)
        log_info(f"Set default gateway to {gateway}.")
    except subprocess.CalledProcessError as e:
        log_error(f"Error setting gateway {gateway}: {e}")

def set_interface_up(interface):
    try:
        subprocess.run(["ip", "link", "set", interface, "up"], check=True)
        log_info(f"Set {interface} up.")
    except subprocess.CalledProcessError as e:
        log_error(f"Error setting {interface} up: {e}")

def set_interface_down(interface):
    try:
        subprocess.run(["ip", "link", "set", interface, "down"], check=True)
        log_info(f"Set {interface} down.")
    except subprocess.CalledProcessError as e:
        log_error(f"Error setting {interface} down: {e}")

def prompt_user_for_interface():
    interfaces = get_network_interfaces()
    print("Available Network Interfaces:")
    print(interfaces)
    interface = input("Enter the interface you want to configure (e.g., eth0, enp3s0): ").strip()
    return interface

def prompt_user_for_ip():
    ip = input("Enter the IP address you want to set: ").strip()
    subnet = input("Enter the subnet mask (e.g., 255.255.255.0): ").strip()
    return ip, subnet

def main_menu():
    while True:
        print("\nNetwork Management Menu:")
        print("1. List Network Interfaces")
        print("2. Add IP Address")
        print("3. Delete IP Address")
        print("4. Set Gateway")
        print("5. Set Interface Up")
        print("6. Set Interface Down")
        print("7. List IP Addresses")
        print("8. Exit")
        
        choice = input("Select an option (1-8): ").strip()
        
        if choice == '1':
            print(get_network_interfaces())
        elif choice == '2':
            interface = prompt_user_for_interface()
            ip, subnet = prompt_user_for_ip()
            add_ip_address(interface, ip, subnet)
        elif choice == '3':
            interface = prompt_user_for_interface()
            ip, subnet = prompt_user_for_ip()
            delete_ip_address(interface, ip, subnet)
        elif choice == '4':
            gateway = input("Enter the gateway: ").strip()
            configure_gateway(gateway)
        elif choice == '5':
            interface = prompt_user_for_interface()
            set_interface_up(interface)
        elif choice == '6':
            interface = prompt_user_for_interface()
            set_interface_down(interface)
        elif choice == '7':
            interface = prompt_user_for_interface()
            list_ip_addresses(interface)
        elif choice == '8':
            log_info("Exiting the network manager.")
            print("Exiting.")
            break
        else:
            log_error("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
