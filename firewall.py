from scapy.all import sniff, IP, TCP
import pydivert
from Utilities.scapy_analyser import *
from Utilities.diversion import *

# Define the firewall rules
BLOCK_ALL = True
BLOCKED_IPS = ["192.168.1.1", "192.168.1.10"]
BLOCKED_PORTS = [80, 443]

# Run Firewall
def run_firewall():
    """
    Intercept and drop packets using pydivert based on rules.
    """
    try:
        divert_packets(BLOCK_ALL,BLOCKED_IPS,BLOCKED_PORTS)
    except KeyboardInterrupt:
        print("\nEXITING FIREWALL.....")
        exit(1)
            

if __name__ == "__main__":
    from threading import Thread

    print("Starting Scapy traffic monitoring...")
    # Start Scapy sniffing in a separate thread for monitoring
    sniff_thread = Thread(target=lambda: sniff(
    filter="ip",
    prn=lambda pkt: scapy_filter_packets(pkt, BLOCK_ALL, BLOCKED_IPS, BLOCKED_PORTS),
    store=0
    ))
    sniff_thread.daemon = True
    sniff_thread.start()

    # Start PyDivert for actual packet interception and blocking
    run_firewall()
