def udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("127.0.0.1", 65433))
    print("UDP Server listening...")
    
    while True:
        data, addr = server.recvfrom(1024)
        if random.random() > 0.1:  # Simulating 10% packet loss
            server.sendto(b"Received: " + data, addr)
    server.close()
