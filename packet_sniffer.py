from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    """
    This function is called for every packet captured.
    It checks if the packet has an IP layer and extracts network details.
    """
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto
        
        # Map protocol numbers to names
        proto_name = "OTHER"
        if proto == 6:
            proto_name = "TCP"
        elif proto == 17:
            proto_name = "UDP"
        elif proto == 1:
            proto_name = "ICMP"
            
        print(f"\n[+] Packet Captured: {src_ip} ➔ {dst_ip} | Protocol: {proto_name}")
        
        # Check for Payload Data
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = bytes(packet.payload)
            if payload:
                print(f"    Payload (Raw Data): {payload[:50]}...") # Print first 50 bytes

def start_sniffer():
    print("--- 🌐 Network Packet Analyzer Started ---")
    print("Listening for network traffic... Press Ctrl+C to stop.")
    
    # Start sniffing (store=0 ensures we don't clog RAM)
    # Note: Requires administrator/root privileges on desktop OS
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    start_sniffer()
