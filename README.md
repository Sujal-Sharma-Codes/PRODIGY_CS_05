# PRODIGY_CS_05
# Network Packet Analyzer 🌐

**A project completed for the Cyber Security Internship at [Prodigy InfoTech](https://prodigyinfotech.dev/).**

## 📝 Project Overview
This repository contains a Python-based network packet analyzer (packet sniffer) built using the Scapy library. The tool captures network packets passing through a network interface and analyzes their headers in real-time. It extracts and displays critical diagnostic information, including source and destination IP addresses, protocol types (TCP, UDP, ICMP), and initial payload data.

## ✨ Features
- **Live Packet Capture:** Listens to network traffic using customizable callback functions.
- **Header Inspection:** Decodes IP layers to identify source and destination endpoints.
- **Protocol Identification:** Maps protocol numbers to readable names (TCP, UDP, ICMP).
- **Payload Extraction:** Inspects the raw byte payload of transport-layer packets.

## 🛠️ Prerequisites
This script requires Python and the `scapy` library.

> **Note:** Packet sniffing requires raw network socket access, which typically needs administrator/root privileges on desktop operating systems (Windows, macOS, Linux). It will not function on mobile sandboxed environments like Android.

Install the required library using pip:

```bash
pip install scapy
```

## 🚀 Usage
1. Download or clone the repository to your desktop machine.
2. Run the script with administrative privileges:
   ```bash
   sudo python packet_sniffer.py  # On Linux/macOS
   # Or run your terminal/IDE as Administrator on Windows
   ```
3. Observe real-time packet information printing to your console.
4. Press `Ctrl + C` to stop the sniffer.

## ⚠️ Ethical & Legal Disclaimer
This tool is strictly for educational purposes, network diagnostics, and authorized security testing.

Unauthorized packet sniffing on networks you do not own or have explicit permission to monitor is illegal and violates privacy laws. Always ensure you have authorization before capturing network traffic.

## 🙏 Acknowledgments
Special thanks to **Prodigy InfoTech** for providing the internship opportunity and an amazing series of cybersecurity challenges!
