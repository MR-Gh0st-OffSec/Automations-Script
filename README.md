# 🚀 Automation Scripts for Ubuntu OS

This repository contains advanced automation scripts designed to streamline various system administration tasks on Ubuntu OS, including port forwarding, auto-scaling, firewall management, IP configuration, and more. Below you'll find a comprehensive usage guide for each script included in this repository.

---

## 🚀 Port Configuration Automation Script

**Description**  

Automates adding, removing, and editing port configurations, including firewall rules and port listening for services on Ubuntu OS.

### 🛠 How to Use

1. **Make the script executable**
   
    ```
    chmod +x port_configurator.py
    ```

3. **Start the script**
   
    ```
    sudo ./port_configurator.py
    ```

5. **Enter Ports**
   
   - The script will prompt for the ports you wish to add or edit.
   - Specify whether you want to open or close each port.

7. **Firewall Rules**
   
   - The script automatically configures firewall rules based on the ports you provide.

9. **Port Listening**
    
   - The script configures port listening for services like Apache2 or Nginx based on your input.

---

## 🔒 Firewall and Port Forwarding Automation (Apache2/Nginx)

**Description**  

Configures and automates port forwarding rules for Apache2 and Nginx in Ubuntu OS.

### 🛠 How to Use

1. **Ensure Apache2 or Nginx is installed**
   
   Make sure Apache2 or Nginx is properly installed and configured.

3. **Make the script executable**
4. 
    ```
    chmod +x port_forwarding_manager.py
    ```

5. **Start the script**
   
    ```
    sudo ./port_forwarding_manager.py
    ```

7. **Choose Services**
   
   - Select either Apache2 or Nginx for port forwarding configuration.
   - Provide the public and private ports.

9. **Firewall Setup**
    
   - The script automatically sets up the forwarding and firewall rules for the selected ports.

---

## 📊 Auto-scaling Management Script

**Description**  

Automates monitoring and scaling of services based on CPU and memory usage thresholds in Ubuntu OS.

### 🛠 How to Use

1. **Make the script executable**
   
    ```
    chmod +x autoscale_manager.py
    ```

3. **Start the script**
   
    ```
    sudo ./autoscale_manager.py
    ```

5. **Threshold Configuration**
   
   - Configure thresholds, instance limits, and other parameters within the script.

7. **Monitoring and Scaling**
   
   - The script monitors CPU and memory usage, automatically scaling services up or down based on the set thresholds.

---

## 🌐 IP Configuration Automation Script

**Description**  

Provides an automated way to manually configure IP addresses for network interfaces on Ubuntu OS.

### 🛠 How to Use

1. **Make the script executable**
   
    ```
    chmod +x ip_configurator.py
    ```

3. **Start the script**
   
    ```
    sudo ./ip_configurator.py
    ```

5. **Configure IP**
   
   - Input the desired IP address when prompted.
   - Choose the network interface (e.g., `eth0`, `wlan0`) to apply the configuration.

6. **Apply Network Settings**
   
   - The script will configure the IP address and restart the network service automatically.

---

## 🔄 System Resource Usage Script

**Description**  

Displays system-wide resource usage, including CPU, memory, disk, and network statistics, to manage and monitor services effectively.

### 🛠 How to Use

1. **Make the script executable**
   
    ```
    chmod +x system_resource_usage.py
    ```

3. **Start the script**
   
    ```
    sudo ./system_resource_usage.py
    ```

5. **View Resource Stats**
   
   - The script displays real-time stats for CPU, memory, disk I/O, and network traffic.
   - Useful for monitoring services and understanding system health.

---

## 🧹 Ubuntu OS Cleanup and Update Script

**Description**  

Automates the cleanup of unused packages, updates the system, and optimizes the Ubuntu environment.

### 🛠 How to Use

1. **Make the script executable**
   
    ```
    chmod +x os_cleanup_updater.py
    ```

3. **Start the script**
   
    ```
    sudo ./os_cleanup_updater.py
    ```

5. **Optimize and Clean**
   
   - The script will remove unnecessary packages and optimize the system's performance.

6. **System Update**
   
   - After the cleanup, the script will prompt you to update the system’s common services, asking for confirmation before proceeding.

---

### 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### 🧑‍💻 Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/MR-Gh0st-OffSec/Automations-Script/issues).

---
