**Transport Layer**
====================

**Introduction**
-----------------

The Transport Layer is responsible for providing reliable data transfer between devices on a network. It ensures that data packets are delivered in the correct order and reassembles them at the receiving end. TCP (Transmission Control Protocol) is one of the primary protocols used in the Transport Layer.

**Core Concepts**
------------------

### Connection Establishment

*   **Three-Way Handshake**: A mechanism to establish a connection between two hosts.
    *   SYN (Sync) bit set to 1 by the client, indicating it wants to initiate a connection.
    *   Server responds with a SYN-ACK (Syn Acknowledgement) packet, which sets its own SYN bit and acknowledges the client's packet. The server also sends its initial sequence number (ISN).
    *   Client sends an ACK (Acknowledgement) packet, acknowledging the server's ISN.

### Congestion Control

*   **TCP Congestion Window**: A variable that limits the amount of data sent by a host.
*   **Slow Start**: An algorithm used to prevent network congestion during connection establishment.
*   **Congestion Avoidance**: An algorithm used to regulate traffic once a TCP connection is established.

**Key Formulas/Theorems**
-------------------------

### TCP Congestion Control

*   $cwnd = \min(\frac{window\_size}{MSS}, cwnd_{max})$

where $cwnd$ is the congestion window, $window\_size$ is the maximum allowed window size, and $MSS$ is the Maximum Segment Size.

**Problem Solving Patterns**
---------------------------

### TCP Connection Establishment

*   Identify whether a connection is being established or an existing connection is being used.
*   Determine which host initiates the connection (client or server).
*   Calculate sequence numbers and acknowledge numbers for each packet.

### Congestion Control

*   Understand the current state of congestion control (slow start, congestion avoidance, or fast recovery).
*   Identify changes in network conditions that may affect congestion control algorithms.

**Examples with Solutions**
---------------------------

### Example 1: TCP Connection Establishment

Suppose a client initiates a connection to a server. The client's initial sequence number is 1000, and the server chooses an initial sequence number of 2000.

#### Step 1: Client Sends SYN Packet

| Field | Value |
| --- | --- |
| SYN bit | 1 |
| Sequence Number | 1000 |

#### Step 2: Server Responds with SYN-ACK Packet

| Field | Value |
| --- | --- |
| SYN bit | 1 |
| ACK bit | 1 |
| Acknowledge Number | 2001 |
| Initial Sequence Number (ISN) | 2000 |

#### Step 3: Client Sends ACK Packet

| Field | Value |
| --- | --- |
| ACK bit | 1 |
| Acknowledge Number | 3001 |

### Example 2: Congestion Control

Suppose a TCP connection has a congestion window of 10,000 bytes. The Maximum Segment Size (MSS) is 1,500 bytes.

#### Step 4: Calculate Congestion Window Size

$cwnd = \min(\frac{window\_size}{MSS}, cwnd_{max})$
$cwnd = \min(\frac{10,000}{1500}, 10,000)$
$cwnd = \min(6.67, 10,000) = 6,670$

**Common Pitfalls**
------------------

*   Forgetting to set the SYN bit when initiating a connection.
*   Misunderstanding sequence numbers and acknowledge numbers during connection establishment.
*   Failing to account for changes in network conditions affecting congestion control.

**Quick Summary**
-----------------

*   TCP Connection Establishment:
    *   Three-way handshake
    *   Sequence number and acknowledge number calculation
*   Congestion Control:
    *   Slow start
    *   Congestion avoidance
    *   Fast recovery