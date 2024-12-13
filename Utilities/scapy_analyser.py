from scapy.all import sniff, IP, TCP

# Scapy packet analysis function
def scapy_filter_packets(packet,BLOCK_ALL,BLOCKED_IPS,BLOCKED_PORTS):
    """
    Analyze packets using Scapy to log the traffic for monitoring.
    """
    try:
        if packet.haslayer(IP):
            src_ip = packet[IP].src
            dest_ip = packet[IP].dst
            dest_port = packet[TCP].dport if packet.haslayer(TCP) else None

            if BLOCK_ALL or src_ip in BLOCKED_IPS or (dest_port in BLOCKED_PORTS if dest_port else False):
                print(f"Scapy: Blocked packet: {src_ip} -> {dest_ip}:{dest_port}")
            else:
                print(f"Scapy: Allowed packet: {src_ip} -> {dest_ip}:{dest_port}")
    except KeyboardInterrupt:
        print("\nEXITING FIREWALL.....")
        exit(1)