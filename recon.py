
import os
import socket
import subprocess
import time
import platform
import requests
from datetime import datetime

# Enhanced Banner for Mr.Infinity
def display_banner():
    banner = r"""
    ███╗   ███╗██████╗     ██╗███╗   ██╗███████╗██╗███╗   ██╗██╗████████╗██╗   ██╗
    ████╗ ████║██╔══██╗    ██║████╗  ██║██╔════╝██║████╗  ██║██║╚══██╔══╝╚██╗ ██╔╝
    ██╔████╔██║██████╔╝    ██║██╔██╗ ██║█████╗  ██║██╔██╗ ██║██║   ██║    ╚████╔╝
    ██║╚██╔╝██║██╔══██╗    ██║██║╚██╗██║██╔══╝  ██║██║╚██╗██║██║   ██║     ╚██╔╝
    ██║ ╚═╝ ██║██║  ██║    ██║██║ ╚████║██║     ██║██║ ╚████║██║   ██║      ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝
                                                           
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |M|r|.|I|n|f|i|n|i|t|y|'|s| |A|d|v|a|n|c|e|d| |R|e|c|o|n| |T|o|o|l|
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    """
    print("\033[1;35m" + banner + "\033[0m")
    print("\033[1;36m[*] Advanced Reconnaissance Toolkit for Termux\033[0m")
    print("\033[1;36m[*] Created by Mr.Infinity\033[0m")
    print("\033[1;36m[*] " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\033[0m\n")

# Check Termux environment
def check_termux():
    try:
        subprocess.check_output(['termux-info'], stderr=subprocess.PIPE)
        return True
    except:
        return False

# Enhanced Network Scanner
def network_scan():
    print("\033[1;34m[+] Performing Advanced Network Scan\033[0m")

    try:
        # Get network interfaces
        print("\n\033[1;33m[+] Network Interfaces:\033[0m")
        interfaces = subprocess.getoutput('ip -o link show')
        print(interfaces)

        # Get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        print(f"\n\033[1;33m[+] Local IP: {local_ip}\033[0m")

        # Get public IP with geolocation
        print("\n\033[1;33m[+] Public IP Information:\033[0m")
        try:
            public_info = requests.get('http://ip-api.com/json/').json()
            print(f"IP: {public_info.get('query', 'N/A')}")
            print(f"ISP: {public_info.get('isp', 'N/A')}")
            print(f"Location: {public_info.get('city', 'N/A')}, {public_info.get('country', 'N/A')}")
            print(f"Coordinates: {public_info.get('lat', 'N/A')}, {public_info.get('lon', 'N/A')}")
        except:
            public_ip = subprocess.getoutput('curl -s ifconfig.me')
            print(f"IP: {public_ip}")

        # ARP scan
        print("\n\033[1;33m[+] ARP Table:\033[0m")
        arp_table = subprocess.getoutput('arp -a')
        print(arp_table if arp_table else "No ARP entries found")

    except Exception as e:
        print(f"\033[1;31m[-] Error in network scan: {e}\033[0m")

# Advanced Port Scanner with service detection
def port_scan(target, ports):
    print(f"\n\033[1;34m[+] Scanning {target} for open ports\033[0m")
    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                print(f"\033[1;32m[+] Port {port} ({service}): OPEN\033[0m")
            else:
                print(f"\033[1;31m[-] Port {port}: CLOSED\033[0m")
            sock.close()
    except Exception as e:
        print(f"\033[1;31m[-] Error in port scan: {e}\033[0m")

# Comprehensive System Information
def system_info():
    print("\n\033[1;34m[+] Gathering Detailed System Information\033[0m")
    try:
        # System information
        print("\n\033[1;33m[+] System Information:\033[0m")
        print(f"System: {platform.system()}")
        print(f"Node Name: {platform.node()}")
        print(f"Release: {platform.release()}")
        print(f"Version: {platform.version()}")
        print(f"Machine: {platform.machine()}")
        print(f"Processor: {platform.processor()}")

        # CPU info
        print("\n\033[1;33m[+] CPU Information:\033[0m")
        cpu_info = subprocess.getoutput('cat /proc/cpuinfo | grep "model name" | head -n 1')
        print(cpu_info.split(':')[1].strip() if cpu_info else "N/A")

        # Memory info
        print("\n\033[1;33m[+] Memory Information:\033[0m")
        mem_total = subprocess.getoutput('cat /proc/meminfo | grep MemTotal')
        mem_free = subprocess.getoutput('cat /proc/meminfo | grep MemFree')
        print(mem_total.split(':')[1].strip() if mem_total else "N/A")
        print(mem_free.split(':')[1].strip() if mem_free else "N/A")

        # Storage info
        print("\n\033[1;33m[+] Storage Information:\033[0m")
        storage = subprocess.getoutput('df -h')
        print(storage)

        # Battery info (for mobile devices)
        print("\n\033[1;33m[+] Battery Information:\033[0m")
        try:
            battery = subprocess.getoutput('termux-battery-status')
            print(battery)
        except:
            print("Battery info not available")

    except Exception as e:
        print(f"\033[1;31m[-] Error gathering system info: {e}\033[0m")

# WHOIS lookup
def whois_lookup(domain):
    print(f"\n\033[1;34m[+] Performing WHOIS lookup for {domain}\033[0m")
    try:
        whois_info = subprocess.getoutput(f'whois {domain}')
        print(whois_info)
    except Exception as e:
        print(f"\033[1;31m[-] Error in WHOIS lookup: {e}\033[0m")

# DNS enumeration
def dns_enum(domain):
    print(f"\n\033[1;34m[+] Performing DNS Enumeration for {domain}\033[0m")
    try:
        print("\n\033[1;33m[+] A Records:\033[0m")
        a_records = subprocess.getoutput(f'dig {domain} A +short')
        print(a_records if a_records else "No A records found")

        print("\n\033[1;33m[+] MX Records:\033[0m")
        mx_records = subprocess.getoutput(f'dig {domain} MX +short')
        print(mx_records if mx_records else "No MX records found")

        print("\n\033[1;33m[+] NS Records:\033[0m")
        ns_records = subprocess.getoutput(f'dig {domain} NS +short')
        print(ns_records if ns_records else "No NS records found")

        print("\n\033[1;33m[+] TXT Records:\033[0m")
        txt_records = subprocess.getoutput(f'dig {domain} TXT +short')
        print(txt_records if txt_records else "No TXT records found")

    except Exception as e:
        print(f"\033[1;31m[-] Error in DNS enumeration: {e}\033[0m")

# Main menu
def main():
    display_banner()

    if not check_termux():
        print("\033[1;31m[-] This script is designed to run on Termux\033[0m")
        return

    while True:
        print("\n\033[1;35m[MAIN MENU]\033[0m")
        print("1. Advanced Network Scan")
        print("2. Port Scan with Service Detection")
        print("3. Comprehensive System Information")
        print("4. WHOIS Lookup")
        print("5. DNS Enumeration")
        print("6. Exit")

        choice = input("\n\033[1;36m[?] Select an option: \033[0m")

        if choice == '1':
            network_scan()
        elif choice == '2':
            target = input("\033[1;36m[?] Enter target IP or hostname: \033[0m")
            ports = input("\033[1;36m[?] Enter ports to scan (comma separated, e.g., 22,80,443): \033[0m")
            ports = [int(p.strip()) for p in ports.split(',')]
            port_scan(target, ports)
        elif choice == '3':
            system_info()
        elif choice == '4':
            domain = input("\033[1;36m[?] Enter domain for WHOIS lookup: \033[0m")
            whois_lookup(domain)
        elif choice == '5':
            domain = input("\033[1;36m[?] Enter domain for DNS Enumeration: \033[0m")
            dns_enum(domain)
        elif choice == '6':
            print("\033[1;32m[+] Exiting... Stay secure Mr.Infinity!\033[0m")
            break
        else:
            print("\033[1;31m[-] Invalid choice. Please try again.\033[0m")

        input("\n\033[1;36m[Press Enter to continue...]\033[0m")

if __name__ == "__main__":
    main()