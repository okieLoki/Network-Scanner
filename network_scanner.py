import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan("172.31.144.1/24")