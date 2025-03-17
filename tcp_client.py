def tcp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 65432))
    latencies = []
    
    for i in range(100):
        msg = f"Message {i}".encode()
        start = time.time()
        client.sendall(msg)
        data = client.recv(1024)
        end = time.time()
        latencies.append(end - start)
        print(data.decode())
    
    print(f"Average TCP Latency: {sum(latencies)/100:.6f} seconds")
    client.close()
