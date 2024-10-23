#!/usr/bin/env python3
import os
import subprocess
import logging

# Author: MR.Gh0st
# Position: Hacker
# Date: 2024-10-22
# Time: 15:00

LOG_FILE = '/var/log/maintenance.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    logging.info(message)
    print(f"[INFO] {message}")

def log_error(message):
    logging.error(message)
    print(f"[ERROR] {message}")

def update_system():
    try:
        log_info("Updating and upgrading the system.")
        subprocess.run(["apt", "update"], check=True)
        subprocess.run(["apt", "upgrade", "-y"], check=True)
        subprocess.run(["apt", "autoremove", "-y"], check=True)
        subprocess.run(["apt", "clean"], check=True)
        log_info("System updated and unnecessary packages removed.")
    except subprocess.CalledProcessError as e:
        log_error(f"Error during system update: {e}")

def list_services():
    try:
        services = subprocess.check_output(["systemctl", "--type=service", "--state=running"]).decode().strip()
        log_info("Listing running services.")
        print(services)
        return services
    except subprocess.CalledProcessError as e:
        log_error(f"Error listing services: {e}")
        return ""

def prompt_service_update():
    update_services = input("Do you want to update common services? (Yes/No): ").strip().lower()
    return update_services in ['yes', 'y']

def update_common_services():
    common_services = [
        "apache2", "mysql", "nginx", "postgresql", "ssh", "docker", 
        "fail2ban", "rsyslog", "cron", "snapd", "ufw", "lighttpd",
        "php7.4-fpm", "redis-server", "memcached", "mongodb", "cassandra", 
        "rabbitmq-server", "prometheus", "grafana", "elasticsearch"
    ]
    for service in common_services:
        try:
            subprocess.run(["apt", "install", "--only-upgrade", service, "-y"], check=True)
            log_info(f"Updated service: {service}")
        except subprocess.CalledProcessError as e:
            log_error(f"Failed to update {service}: {e}")

def display_disk_usage():
    try:
        usage = subprocess.check_output(["df", "-h"]).decode().strip()
        log_info("Displaying disk usage.")
        print(usage)
    except subprocess.CalledProcessError as e:
        log_error(f"Error displaying disk usage: {e}")

def main():
    update_system()
    services = list_services()
    
    if services:
        if prompt_service_update():
            update_common_services()
            log_info("Common services updated.")
        else:
            log_info("User chose not to update common services.")

    display_disk_usage()
    log_info("Maintenance tasks completed.")

if __name__ == "__main__":
    main()
