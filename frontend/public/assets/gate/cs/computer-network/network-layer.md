**Network Layer**
================

### Introduction
-----------------

The Network Layer is responsible for routing and forwarding packets between devices on a network. It ensures that data reaches its intended destination, handling tasks such as packet switching, routing, and congestion control.

### Core Concepts
------------------

#### Fragmentation and Reassembly
---------------------------------

Fragmentation occurs when a device breaks down a large IP datagram into smaller pieces to fit within the MTU (Maximum Transmission Unit) of the network. This process is typically performed at the source or intermediate routers if necessary.

The reassembly process involves reconstructing the original datagram from its fragments at the destination device.

#### IPv4 Fragmentation
----------------------

According to RFC 791, IPv4 fragmentation can occur at multiple points along the path:

*   The source device may fragment a packet that exceeds the MTU of the outgoing link.
*   Intermediate routers may also fragment packets if they exceed the MTU of their outgoing links.

Fragmentation involves splitting the datagram into fragments, which are then sent over the network. Each fragment includes:

1.  A Fragment Header (8 bytes)
2.  The original packet's header and data
3.  A Fragment Offset field, indicating the position of this fragment within the original packet

The reassembly process at the destination device involves matching incoming fragments to the correct datagram based on their Fragment Identifier fields.

#### MTU and Packet Size
-------------------------

MTU (Maximum Transmission Unit) is the maximum size of a packet that can be transmitted over a network link without fragmentation. The MTU varies between networks, ranging from 576 bytes for Ethernet to larger values for other technologies.

When sending data over multiple links with different MTUs, it's essential to consider the smallest MTU along the path to avoid fragmentation.

### Key Formulas/Theorems
---------------------------

No specific formulas are required for this topic; however, understanding of packet sizes and MTUs is crucial for successful fragmentation and reassembly.

### Problem Solving Patterns
-----------------------------

When solving questions related to network layer concepts:

*   Pay attention to the details: Be aware of the specific requirements mentioned in each question.
*   Analyze the problem: Break down the problem into smaller parts, considering the specifics of each scenario.
*   Consider multiple possibilities: When dealing with packet fragmentation and reassembly, be prepared for different outcomes based on various network conditions.

### Examples with Solutions
---------------------------

**Example 1: IPv4 Fragmentation**

Suppose we need to send an IP datagram of size 1420 bytes (including a 20-byte header) over two links with MTUs of 542 bytes and 360 bytes, respectively. Determine the number of fragments that would be delivered at the receiver.

| Link | MTU |
| --- | --- |
| A    | 542 |
| B    | 360 |

To fit within the smaller MTU of link B (360 bytes), we must fragment the datagram:

*   Fragment size = minimum(MTU A, MTU B) = 360 bytes
*   Number of fragments = (Total packet size - Header) / Fragment size
= \[ (1420-20) \div 360 \] 

\[ 1400\div360 \]

\[3+16/360 \approx4.044 \]

Since data must be a multiple of 8, we round up to the nearest whole number:

Number of fragments = 5

### Common Pitfalls
--------------------

*   Failing to consider the smallest MTU along the path when dealing with packet fragmentation.
*   Misunderstanding the process of reassembly at the destination device.

### Quick Summary
------------------

*   IPv4 fragmentation can occur at multiple points, including source devices and intermediate routers.
*   Reassembly occurs at the destination device, where incoming fragments are matched to the correct datagram based on their Fragment Identifier fields.
*   When dealing with packet sizes and MTUs, consider the smallest MTU along the path to avoid fragmentation.

Note: This theory note covers essential concepts related to network layer in computer networks. Students can use it as a reference for studying and revising before the GATE CS exam.