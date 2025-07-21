#!/bin/bash

# Colors
g="\033[1;32m"
r="\033[1;31m"
y="\033[1;33m"
c="\033[1;36m"
w="\033[0m"

# Clear screen
clear

# ASCII Banner
echo -e "${c}"
echo "______                 _____       __ _       _ _         "
echo "| ___ \               |_   _|     / _(_)     (_) |        "
echo "| |_/ / ___  ___ ___    | | _ __ | |_ _ _ __  _| |_ _   _  "
echo "| ___ \/ _ \/ __/ __|   | || '_ \|  _| | '_ \| | __| | | | "
echo "| |_/ / (_) \__ \__ \  _| || | | | | | | | | | | |_| |_| | "
echo "\____/ \___/|___/___/  \___/_| |_|_| |_|_| |_|_|\__|\__, | "
echo "                                                    __/ | "
echo "                                                   |___/  "
echo -e "${w}"
echo -e "${y}           Created by: ☠️ (Mr. Infinity)☠️${w}"
echo -e "${c}=========================================================${w}"
echo

# Menu
while true; do
    echo -e "${g}[1]${w} Update System"
    echo -e "${g}[2]${w} Install Basic Packages"
    echo -e "${g}[3]${w} Port Scanner"
    echo -e "${g}[4]${w} IP Tracker"
    echo -e "${g}[5]${w} Device Info"
    echo -e "${g}[0]${w} Exit"
    echo
    read -p "Choose an option: " opt

    case $opt in
        1)
            echo -e "${y}Updating Termux...${w}"
            pkg update -y && pkg upgrade -y
            ;;
        2)
            echo -e "${y}Installing basic packages...${w}"
            pkg install -y curl wget git python nmap neofetch
            ;;
        3)
            read -p "Enter target IP/Domain: " target
            nmap $target
            ;;
        4)
            read -p "Enter IP to track: " ip
            curl http://ip-api.com/json/$ip
            ;;
        5)
            echo -e "${y}Device Info:${w}"
            neofetch
            ;;
        0)
            echo -e "${r}Exiting...${w}"
            break
            ;;
        *)
            echo -e "${r}Invalid Option! Try again.${w}"
            ;;
    esac
    echo
done