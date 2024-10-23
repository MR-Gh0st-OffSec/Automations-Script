#!/usr/bin/env python3
import os
import subprocess
import sys
import logging

# Author: MR.Gh0st
# Position: Hacker
# Date: 2024-10-22
# Time: 16:30

LOG_FILE = '/var/log/port_forwarding_manager.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    logging.info(message)
    print(f"[INFO] {message}")

def log_error(message):
    logging.error(message)
    print(f"[ERROR] {message}")

def check_apache_installed():
    try:
        subprocess.check_output(["apache2ctl", "-v"])
        return True
    except subprocess.CalledProcessError:
        return False

def check_nginx_installed():
    try:
        subprocess.check_output(["nginx", "-v"])
        return True
    except subprocess.CalledProcessError:
        return False

def prompt_for_server_type():
    while True:
        server_type = input("Choose server type (Apache or Nginx): ").strip().lower()
        if server_type in ['apache', 'nginx']:
            return server_type
        else:
            log_error("Invalid server type. Please enter either 'Apache' or 'Nginx'.")

def prompt_for_ports():
    external_port = input("Enter the external port: ").strip()
    internal_port = input("Enter the internal port: ").strip()
    return external_port, internal_port

def update_apache_config(external_port, internal_port):
    config_path = '/etc/apache2/sites-available/000-default.conf'
    try:
        with open(config_path, 'a') as config_file:
            config_file.write(f"\nListen {external_port}\n")
            config_file.write(f"<VirtualHost *:{external_port}>\n")
            config_file.write(f"    ProxyPass / http://localhost:{internal_port}/\n")
            config_file.write(f"    ProxyPassReverse / http://localhost:{internal_port}/\n")
            config_file.write(f"</VirtualHost>\n")
        
        subprocess.run(["a2enmod", "proxy"], check=True)
        subprocess.run(["a2enmod", "proxy_http"], check=True)
        log_info(f"Updated Apache configuration to forward port {external_port} to {internal_port}.")
    except Exception as e:
        log_error(f"Error updating Apache configuration: {e}")
        sys.exit(1)

def update_nginx_config(external_port, internal_port):
    config_path = '/etc/nginx/sites-available/default'
    try:
        with open(config_path, 'a') as config_file:
            config_file.write(f"\nserver {{\n")
            config_file.write(f"    listen {external_port};\n")
            config_file.write(f"    location / {{\n")
            config_file.write(f"        proxy_pass http://localhost:{internal_port};\n")
            config_file.write(f"        proxy_set_header Host $host;\n")
            config_file.write(f"        proxy_set_header X-Real-IP $remote_addr;\n")
            config_file.write(f"        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;\n")
            config_file.write(f"    }}\n")
            config_file.write(f"}}\n")

        log_info(f"Updated Nginx configuration to forward port {external_port} to {internal_port}.")
    except Exception as e:
        log_error(f"Error updating Nginx configuration: {e}")
        sys.exit(1)

def restart_services(server_type):
    try:
        if server_type == 'apache':
            subprocess.run(["systemctl", "restart", "apache2"], check=True)
            log_info("Restarted Apache service.")
        elif server_type == 'nginx':
            subprocess.run(["systemctl", "restart", "nginx"], check=True)
            log_info("Restarted Nginx service.")
    except subprocess.CalledProcessError as e:
        log_error(f"Error restarting {server_type} service: {e}")

def main():
    server_type = prompt_for_server_type()
    
    if server_type == 'apache' and not check_apache_installed():
        log_error("Apache is not installed on this system.")
        sys.exit(1)
    elif server_type == 'nginx' and not check_nginx_installed():
        log_error("Nginx is not installed on this system.")
        sys.exit(1)

    external_port, internal_port = prompt_for_ports()
    
    if server_type == 'apache':
        update_apache_config(external_port, internal_port)
    elif server_type == 'nginx':
        update_nginx_config(external_port, internal_port)

    restart_services(server_type)
    log_info("Port forwarding configuration completed successfully.")

if __name__ == "__main__":
    main()