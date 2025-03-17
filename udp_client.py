def udp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    latencies = []
    lost_packets = 0
    
    for i in range(100):
        msg = f"Message {i}".encode()
        start = time.time()
        client.sendto(msg, ("127.0.0.1", 65433))
        try:
            client.settimeout(0.1)
            data, _ = client.recvfrom(1024)
            end = time.time()
            latencies.append(end - start)
            print(data.decode())
        except socket.timeout:
            lost_packets += 1
    
    print(f"Average UDP Latency: {sum(latencies)/len(latencies):.6f} seconds")
    print(f"Packet Loss Rate: {lost_packets}%")
    client.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "tcp_server":
            tcp_server()
        elif sys.argv[1] == "tcp_client":
            tcp_client()
        elif sys.argv[1] == "udp_server":
            udp_server()
        elif sys.argv[1] == "udp_client":
            udp_client()
