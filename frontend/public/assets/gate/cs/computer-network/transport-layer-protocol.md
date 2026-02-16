# Transport Layer Protocol
==========================

## Introduction
---------------

The transport layer protocol, also known as TCP/IP (Transmission Control Protocol/Internet Protocol), is a crucial component of the OSI (Open Systems Interconnection) model. It ensures reliable data transfer between devices on a network by providing segmentation, acknowledgment, and flow control.

## Core Concepts
-----------------

### Connection-Oriented vs Connectionless

*   **Connection-oriented**: Establishes a dedicated connection before transmitting data.
*   **Connectionless**: Transmits data without establishing a prior connection (e.g., UDP).

### TCP Segment Structure

A TCP segment consists of the following:

1.  **Source Port** (`16` bits): Identifies the process on the sender's machine that originated the data.
2.  **Destination Port** (`16` bits): Identifies the process on the receiver's machine that will receive the data.
3.  **Sequence Number** (`32` bits): Tracks the order of segments transmitted by the sender.
4.  **Acknowledgment Number** (`32` bits): Acknowledges the receipt of data from the sender.
5.  **Header Length** (`16` bits): Indicates the length of the header in `32-bit` words.

### TCP Connection States

A TCP connection can be in one of several states:

1.  **SYN SENT**: The client initiates a connection by sending a SYN packet to the server.
2.  **SYN RECEIVED**: The server responds with its own SYN packet and acknowledges the client's initial SYN.
3.  **ESTABLISHED**: Data transfer occurs between the client and server.
4.  **FIN WAIT 1**: The client sends a FIN packet, indicating it has completed sending data.
5.  **TIME WAIT**: The client waits for the other end to acknowledge its last transmission.

## Key Formulas/Theorems
---------------------------

### TCP Connection Establishment

The process involves three-way handshake:

$$ \text{SYN} \to \text{Client} \to \text{Server: SYN ACK} \to \text{Client: ACK} $$

### TCP Segment Ordering

The sender uses sequence numbers to ensure correct ordering of segments.

## Problem Solving Patterns
---------------------------

*   Analyze the given scenario and identify the relevant TCP concepts.
*   Determine the initial state of the connection (e.g., established, closed).
*   Identify any data exchange or acknowledgment issues that may have occurred due to the server crash.

## Examples with Solutions

### Example 1: TCP Connection Establishment

A client initiates a connection to a server by sending a SYN packet. The server responds with its own SYN ACK packet and an acknowledgment of the client's initial SYN.

Solution:

Client sends SYN packet (SYN = 0x01, Seq = 100)

Server receives SYN packet, generates response SYN ACK packet (SYN ACK = 0x02, Ack = 101), and sends it back to the client.

### Example 2: TCP Segment Ordering

A sender transmits two segments with sequence numbers 200 and 300. The receiver acknowledges receipt of these segments by sending an ACK packet with acknowledgment number 301.

Solution:

Sender A: Segments (Seq = 200, Data)

Sender A: Segments (Seq = 300, Data)

Receiver B: ACK Packet (Ack = 301)

## Common Pitfalls
-------------------

*   Failing to account for TCP connection states and segment ordering.
*   Ignoring the impact of network partitions or crashes on data transfer.

## Quick Summary
----------------

Key points to remember:

*   TCP is a connection-oriented protocol that provides reliable data transfer.
*   The three-way handshake establishes a TCP connection between client and server.
*   Sequence numbers ensure correct ordering of segments transmitted by the sender.