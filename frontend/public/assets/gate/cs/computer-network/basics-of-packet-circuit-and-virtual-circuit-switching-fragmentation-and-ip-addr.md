**Basics of Packet Circuit and Virtual Circuit Switching, Fragmentation, and IP Addressing**
===========================================================

### Introduction
Computer networks rely on switching mechanisms to forward packets between nodes. Two primary types are packet circuit (PC) and virtual circuit (VC) switching. We will explore these concepts along with fragmentation and IP addressing.

### Core Concepts

#### Packet Circuit Switching (PCS)

In PCS, each incoming packet is routed based solely on its header information. The receiving node makes forwarding decisions without prior knowledge of the data's path or destination. Packets may follow different routes to reach their destination, increasing latency.

```mermaid
graph LR
A[Sender] --> B[Routing Decision]
B --> C[Forwarding]
C --> D[Receiver]
```

#### Virtual Circuit Switching (VCS)

In VCS, a connection is established before data transmission begins. The routing information is exchanged between nodes at the start of each session. Packets follow the same path to their destination, reducing latency.

```mermaid
graph LR
A[Sender] --> B[Routing Decision]
B --> C[Connection Establishment]
C --> D[Data Transmission]
```

#### Fragmentation

Fragmentation is the process of dividing a packet into smaller units (fragments) when it exceeds the maximum transmission unit (MTU) of an interface. This allows for more efficient transmission over networks with varying MTUs.

### Key Formulas/Theorems

- **Packet Transmission Time**: The time taken for a receiver to completely receive a packet is given by:

$$ t = \frac{s}{r} $$

where $s$ is the size of the packet and $r$ is the link bandwidth.

```latex
t = \frac{s}{r}
```

### Problem Solving Patterns

- **Analyzing Network Latency**: Identify whether PCS or VCS is used, then determine if fragmentation occurs.
- **Calculating Packet Transmission Time**: Use the formula above with given packet size and link bandwidth values.

### Examples with Solutions

**Q1 (ID: cs_2022_2)**

Consider a 100 Mbps link between an earth station (sender) and a satellite (receiver) at an altitude of 2100 km. The signal propagates at a speed of 8.3 x 10^m/s. The time taken (in milliseconds, rounded to two decimal places) for the receiver to completely receive a packet of 1000 bytes transmitted by the sender is ____.

- **Step 1**: Convert link bandwidth from Mbps to bits per second:

$$ r = 100 \times 10^6 \text{ bps} $$

- **Step 2**: Calculate packet transmission time using the formula above:

$$ t = \frac{s}{r} = \frac{1000 \text{ bytes}}{1.00 \times 10^8 \text{ bps}} \approx 7.07 \times 10^{-5} \text{ s} $$

- **Step 3**: Convert transmission time from seconds to milliseconds:

$$ t \approx 7.07 \times 10^{-5} \text{ s} \times 1000 \frac{\text{ms}}{\text{s}} = 70.7 \text{ ms} $$

**Solution**: The receiver takes approximately 7.08 ms to receive the packet.

### Common Pitfalls

- **Incorrect Unit Conversions**: Ensure proper conversion between units (e.g., bits per second to bytes per second).
- **Oversight of Packet Size or Link Bandwidth**: Double-check given values in problem statements.

### Quick Summary
* Packet Circuit Switching: each incoming packet is routed based on its header information.
* Virtual Circuit Switching: connection established before data transmission, packets follow same path.
* Fragmentation: dividing packets into smaller units when exceeding MTU of an interface.
* Key Formula: $t = \frac{s}{r}$ for packet transmission time.