
from scapy.all import *
import os

#Flexibility for additonal options in the future
option_list = [1, 2, 3, 4]

#functions
#cmd = 'ipconfig'
#os.system(cmd)

def execute_windows_cmd():
    cmd = input("Enter Windows Command > ")
    try:
        os.system(cmd)
    except:
        print("Windows Command Failed")

def show_interfaces():
    print("Printing Interfaces")
    print(conf.ifaces)
    print("Printing Default Interfaces")
    print(conf.iface)

def show_routes():
    #IPv4 routes
    print("\nprinting IPv4 routes...")
    print(conf.route)
    #IPv6 routes
    print("\nprinting IPv6 routes...")
    print(conf.route6)

def sniff_packets():
    print("How pany packets would you like to sniff?")
    num = input("> ")
    num = int(num)
    packet = sniff(count=num)
    print("Packet Summary...")
    packet.nsummary() #print packet summary
    pCount = 0
    for p in packet:
        pCount += 1 #get the amount of packets captured
    print(str(pCount) + " packets captured.")
    pShow = input("Which packets would you like to show? (Separated by a Space): ")
    pShow_list = pShow.split(' ')
    print(pShow_list)
    for i in range(len(pShow_list)):
        print("\nPacket " + pShow_list[i])
        pShow_list[i] = int(pShow_list[i])
        packet[pShow_list[i]].show() 


def scapy_program():
    print("Welcome to the Scapy Automation Tool")
    print(
    '''
    1. Execute Windows Command
    2. Show Interfaces
    3. Show Routes
    4. Sniff Packets
    '''
    )
    option = input("> ")
    option = int(option)
    if option in option_list:
        if option == 1:
            execute_windows_cmd()
        if option == 2:
            show_interfaces()
        if option == 3:
            show_routes()
        if option == 4:
            sniff_packets()

scapy_program()

"""

#get route for a specific IP
print("\nprinting route for a specific IP...")
print(conf.route.route("192.168.1.86"))

#get router IP address
print("\nprinting router IP address...")
get_router = conf.route.route("0.0.0.0")[2]
print(get_router) 

#get local IP / IP of an interface
print("\nprinting local IP / IP of an interface...")
ip = get_if_addr(conf.iface) #default interface
print(ip)

#get local MAC / MAC of an interface
mac = get_if_hwaddr(conf.iface) #default interface
mac2= get_if_hwaddr("Realtek PCIe GbE Family Controller") #this also
print("\nprinting MAC address of default interface...")
print(mac)

#return working interfaces

print("\nprinting working interfaces...)
work = scapy.interfaces.get_if_list()
for interface in work:
    print(interface)

#creating packets
#===============#
#send ICMP packet
print("sending ICMP packet...")
send(IP(src="192.168.1.86",dst="192.168.1.254")/ICMP()/"Chungus")

print("\ncreating a packet...")
#create packet in one line
packet = Ether()/IP(dst='8.8.8.8')/TCP(dport=53,flags='S')
print(packet)
#send(packet)
"""
