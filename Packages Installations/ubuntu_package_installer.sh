#!/bin/bash

# Author: MR.Gh0st
# Position: Hacker
# Date: 2024-10-22

function ask_installation {
    package_name=$1
    echo -n "Do you want to install $package_name (yes / no)? "
    read answer
    if [ "$answer" == "yes" ]; then
        sudo apt install -y $package_name
        echo "$package_name has been installed successfully."
    else
        echo "Skipping $package_name installation."
    fi
}

function install_web_server_packages {
    echo "Installing Web Server Packages..."
    ask_installation "apache2"
    ask_installation "nginx"
    ask_installation "mysql-server"
    ask_installation "php"
    ask_installation "php-mysql"
    ask_installation "php-fpm"
    ask_installation "php-curl"
    ask_installation "php-json"
    ask_installation "php-xml"
    ask_installation "php-gd"
    ask_installation "libapache2-mod-php"
    ask_installation "php-cli"
    ask_installation "php-mbstring"
    ask_installation "php-zip"
    ask_installation "php-soap"
    ask_installation "php-intl"
    ask_installation "php-bcmath"
    ask_installation "certbot"
    ask_installation "python3-certbot-apache"
}

function install_management_tools {
    echo "Installing Management Tools..."
    ask_installation "htop"
    ask_installation "net-tools"
    ask_installation "ufw"
    ask_installation "fail2ban"
    ask_installation "monit"
    ask_installation "logwatch"
    ask_installation "cron"
    ask_installation "rsyslog"
    ask_installation "nagios-nrpe-server"
    ask_installation "git"
    ask_installation "screen"
    ask_installation "bmon"
    ask_installation "glances"
    ask_installation "iotop"
    ask_installation "ncdu"
    ask_installation "ntp"
    ask_installation "sysstat"
}

function install_development_tools {
    echo "Installing Development Tools..."
    ask_installation "build-essential"
    ask_installation "git"
    ask_installation "vim"
    ask_installation "python3"
    ask_installation "python3-pip"
    ask_installation "docker.io"
    ask_installation "docker-compose"
    ask_installation "nodejs"
    ask_installation "npm"
    ask_installation "ruby"
    ask_installation "golang"
    ask_installation "java"
    ask_installation "maven"
    ask_installation "gradle"
    ask_installation "perl"
    ask_installation "php"
    ask_installation "elixir"
    ask_installation "flutter"
    ask_installation "rustc"
    ask_installation "cargo"
    ask_installation "postman"
}

function install_system_tools {
    echo "Installing System Tools..."
    ask_installation "curl"
    ask_installation "wget"
    ask_installation "unzip"
    ask_installation "zip"
    ask_installation "software-properties-common"
    ask_installation "snapd"
    ask_installation "parted"
    ask_installation "fdisk"
    ask_installation "lvm2"
    ask_installation "tmux"
    ask_installation "tree"
    ask_installation "chkrootkit"
    ask_installation "rkhunter"
    ask_installation "auditd"
    ask_installation "sysdig"
    ask_installation "dstat"
    ask_installation "iotop"
}

function install_network_tools {
    echo "Installing Network Tools..."
    ask_installation "nmap"
    ask_installation "traceroute"
    ask_installation "iperf3"
    ask_installation "tcpdump"
    ask_installation "telnet"
    ask_installation "dnsutils"
    ask_installation "openssh-server"
    ask_installation "openvpn"
    ask_installation "bridge-utils"
    ask_installation "wireguard"
    ask_installation "netcat"
    ask_installation "iftop"
    ask_installation "curlftpfs"
    ask_installation "mtr"
    ask_installation "socat"
    ask_installation "whois"
    ask_installation "iw"
    ask_installation "netstat-nat"
}

function main {
    echo "Welcome to the Ubuntu Package Installer!"

    echo "Select which packages you want to install:"
    echo "1) Web Server Packages"
    echo "2) Management Tools"
    echo "3) Development Tools"
    echo "4) System Tools"
    echo "5) Network Tools"
    echo "6) Install All Packages"

    read -p "Enter your selection: " selection

    case $selection in
        1)
            install_web_server_packages
            ;;
        2)
            install_management_tools
            ;;
        3)
            install_development_tools
            ;;
        4)
            install_system_tools
            ;;
        5)
            install_network_tools
            ;;
        6)
            install_web_server_packages
            install_management_tools
            install_development_tools
            install_system_tools
            install_network_tools
            ;;
        *)
            echo "Invalid selection. Exiting."
            exit 1
            ;;
    esac

    echo "Package installation completed."
}

main
