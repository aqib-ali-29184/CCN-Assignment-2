# CCN-Assignment-2

# Socket Programming: TCP vs. UDP Comparison

## Overview
This project compares TCP and UDP by implementing client-server applications that measure latency, packet loss, and throughput.

## Files
- `tcp_server.py` - TCP server that listens for connections and responds to messages.
- `tcp_client.py` - TCP client that sends messages and measures round-trip time.
- `udp_server.py` - UDP server that listens for packets and simulates packet loss.
- `udp_client.py` - UDP client that sends messages and records latency & loss rate.
- `tcp_log.txt` - Log file containing TCP communication records.
- `udp_log.txt` - Log file containing UDP communication records.

## How to Run
Ensure Python is installed and execute the following commands in separate terminals:

1. Start the TCP server:
   ```sh
   python socket_programming.py tcp_server
   ```

2. Run the TCP client:
   ```sh
   python socket_programming.py tcp_client
   ```

3. Start the UDP server:
   ```sh
   python socket_programming.py udp_server
   ```

4. Run the UDP client:
   ```sh
   python socket_programming.py udp_client
   ```

## Expected Outputs
- TCP Client: Receives acknowledgment for all messages and measures average latency.
- UDP Client: Some messages may be lost, and it calculates the packet loss rate.

## Observations
### Latency Comparison
- TCP has higher latency due to connection setup and acknowledgments.
- UDP has lower latency but may experience packet loss.

### Reliability and Packet Loss
- TCP ensures message delivery with retransmissions.
- UDP may drop packets, leading to occasional data loss.

### Throughput Analysis
- TCP has lower throughput due to acknowledgments.
- UDP is faster for real-time applications but unreliable.

## Use Cases
- **TCP**: Web browsing, file transfer (HTTP, FTP, SSH).
- **UDP**: Streaming, VoIP, gaming (DNS, video calls).

## References
- Python socket programming documentation.
- Network protocol guides and online resources.
