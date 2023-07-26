from scapy.all import *
p = sr1(IP(dst="192.168.1.254")/ICMP()/"XXXXXXXXXXX")
p.show()
