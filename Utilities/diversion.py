import pydivert


def divert_packets(BLOCK_ALL,BLOCKED_IPS,BLOCKED_PORTS):
    """
    Intercept and drop packets using pydivert based on rules.
    """
    try:
        print("Starting PyDivert for packet interception...")
        with pydivert.WinDivert("ip") as w:
            for packet in w:
                if BLOCK_ALL or packet.src_addr in BLOCKED_IPS or packet.dst_port in BLOCKED_PORTS:
                    print(f"PyDivert: Dropped packet from {packet.src_addr} to {packet.dst_addr}:{packet.dst_port}")
                    # Drop the packet by not reinjecting it
                else:
                    print(f"PyDivert: Allowed packet from {packet.src_addr} to {packet.dst_addr}:{packet.dst_port}")
                    w.send(packet)  # Reinject to allow the packet
    except KeyboardInterrupt:
        print("\nEXITING FIREWALL.....")
        exit(1)