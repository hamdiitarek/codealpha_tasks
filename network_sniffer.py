from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto
        
        if TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            payload_size = len(packet[TCP].payload)
            print(f"TCP  {ip_src}:{sport} -> {ip_dst}:{dport}  Payload size: {payload_size} bytes")
        
        elif UDP in packet:
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            payload_size = len(packet[UDP].payload)
            print(f"UDP  {ip_src}:{sport} -> {ip_dst}:{dport}  Payload size: {payload_size} bytes")
        
        else:
            print(f"IP  {ip_src} -> {ip_dst}  Protocol: {proto}")

def main():
    print("Starting packet sniffer...")
    # conf.L3socket = L3PacketSocket
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()