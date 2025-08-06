# capture.py
from scapy.all import sniff

def packet_handler(packet):
    """
    This function will be called for each captured packet.
    """
    print("Packet captured:")
    print(packet.summary()) # .summary() gives a one-line description

print("Starting network sniffer...")
# Sniff 10 packets and then stop.
sniff(count=10, prn=packet_handler)
print("Sniffing complete.")