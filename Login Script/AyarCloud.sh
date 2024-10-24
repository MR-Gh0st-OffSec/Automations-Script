#!/bin/bash

# Clear the screen for dramatic effect
clear

# Display Mr.Gh0st ASCII Art

cat << "EOF"
      _                       ____ _                 _
     / \  _   _  __ _ _ __   / ___| | ___  _   _  __| |
    / _ \| | | |/ _` | '__| | |   | |/ _ \| | | |/ _` |
   / ___ \ |_| | (_| | |    | |___| | (_) | |_| | (_| |
  /_/   \_\__, |\__,_|_|     \____|_|\___/ \__,_|\__,_|
          |___/
EOF
echo " "
echo " "
echo " "
echo "      Welcome, Mr.Gh0st..."
echo "      Your system awaits your command."
echo " "
echo " "

# Show current date and time
echo "📅 Date: $(date)"
echo "🌐 Host: $(hostname)"
echo "💻 Logged in as: $USER"

# Display some system information
echo " "
echo "SYSTEM INFORMATION:"
echo "-------------------"
echo "🖥️ OS Version: $(lsb_release -d | cut -f2)"
echo "🖱️  Uptime: $(uptime -p)"
echo "🔥 CPU Load: $(cat /proc/loadavg | awk '{print $1, $2, $3}')"
echo "💾 Memory Usage: $(free -m | awk 'NR==2{printf "Used: %sMB / Total: %sMB", $3,$2}')"
echo " "

# Function to display open ports
function show_open_ports {
    echo "OPEN PORTS:"
    echo "------------"
    echo "Proto |  Local Address      |  State"
    echo "----------------------------------------"
    netstat -tuln | awk 'NR>2 {printf "%-5s | %-18s | %s\n", $1, $4, $6}'
}

# Function to display interface status
function show_interface_status {
    echo "INTERFACE STATUS:"
    echo "-----------------"
    echo "Interface | Status"
    echo "--------------------"
    ip a | awk '/^[0-9]+: / {print $2}' | sed 's/://g' | while read -r iface; do
        state=$(cat /sys/class/net/$iface/operstate)
        printf "%-10s | %s\n" "$iface" "$state"
    done
}

# Function to display a simple bar chart


# Call functions to display information
show_open_ports
echo " "
show_service_status
echo " "
show_interface_status
echo " "
show_bar_chart
echo " "

# Final message
echo "❯❯❯ Awaiting your next move, Mr.Gh0st..."
echo " "
