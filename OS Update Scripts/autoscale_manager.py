#!/usr/bin/env python3
import os
import psutil
import subprocess
import time
import logging

# Author: MR.Gh0st
# Position: Hacker
# Date: 2024-10-22
# Time: 18:00

LOG_FILE = '/var/log/autoscale_manager.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Thresholds for CPU and Memory usage (in percentage)
CPU_THRESHOLD = 80  # CPU threshold for scaling (in %)
MEMORY_THRESHOLD = 75  # Memory threshold for scaling (in %)
SCALE_UP_WAIT_TIME = 60  # Time to wait before scaling up (in seconds)
SCALE_DOWN_WAIT_TIME = 300  # Time to wait before scaling down (in seconds)

# Limits for scaling
MAX_INSTANCES = 5  # Maximum number of instances allowed
MIN_INSTANCES = 1  # Minimum number of instances allowed

# Service name to scale
SERVICE_NAME = 'my_app_service'  # Replace with your service name

def log_info(message):
    logging.info(message)
    print(f"[INFO] {message}")

def log_error(message):
    logging.error(message)
    print(f"[ERROR] {message}")

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_running_instances(service_name):
    try:
        result = subprocess.check_output(
            ["pgrep", "-f", service_name], universal_newlines=True)
        pids = result.strip().split("\n")
        return len(pids)
    except subprocess.CalledProcessError:
        return 0

def scale_up(service_name):
    current_instances = get_running_instances(service_name)
    if current_instances < MAX_INSTANCES:
        log_info(f"Scaling up {service_name}. Current instances: {current_instances}")
        os.system(f"systemctl start {service_name}@{current_instances + 1}")
    else:
        log_info(f"Max instances reached for {service_name}. Cannot scale up further.")

def scale_down(service_name):
    current_instances = get_running_instances(service_name)
    if current_instances > MIN_INSTANCES:
        log_info(f"Scaling down {service_name}. Current instances: {current_instances}")
        os.system(f"systemctl stop {service_name}@{current_instances}")
    else:
        log_info(f"Min instances reached for {service_name}. Cannot scale down further.")

def monitor_and_scale():
    while True:
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        log_info(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%")

        if cpu_usage > CPU_THRESHOLD or memory_usage > MEMORY_THRESHOLD:
            log_info("Resource usage high. Scaling up...")
            scale_up(SERVICE_NAME)
            time.sleep(SCALE_UP_WAIT_TIME)
        else:
            log_info("Resource usage low. Scaling down...")
            scale_down(SERVICE_NAME)
            time.sleep(SCALE_DOWN_WAIT_TIME)

def main():
    log_info("Starting auto-scaling script.")
    monitor_and_scale()

if __name__ == "__main__":
    main()
