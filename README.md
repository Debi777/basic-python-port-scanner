# Basic Python Port Scanner

A Python-based network tool designed to scan and identify open ports on a target IP address. 

Whether you are a user looking to quickly check for open services on a machine, or a recruiter reviewing my cybersecurity portfolio, this repository provides a lightweight, easy-to-read network scanning utility.

## 🚀 How to Use (For Users)

You can run this script directly from your command line to test for open ports on a specific IP address. It will check common ports (20-100) and report back any that are actively listening.

**Prerequisites:** 
- Python 3 installed on your system.

**Usage Syntax:**
`python port_scanner.py <target_ip>`

**Example (Scanning your local machine):**
`python port_scanner.py 127.0.0.1`

> **⚠️ Security & Ethics Warning:** Never run a port scanner against a website, IP address, or network that you do not own or have explicit permission to test. Unauthorized scanning is unethical and may be illegal.

---

## 🛠️ Project Details (For Portfolio Review)

### Objective
The core goal of this project is to demonstrate a foundational understanding of networking protocols (TCP/IP) and Python scripting. Identifying open ports is the first step in network reconnaissance, revealing potential entry points, vulnerabilities, or running services.

### Skills Demonstrated
- **Network Socket Programming:** Utilizing Python's built-in libraries to establish TCP connections.
- **TCP/IP Fundamentals:** Practical understanding of TCP handshakes, ports, and connection timeouts.
- **Error Handling:** Implementing `try/except` blocks to gracefully manage DNS resolution failures, dropped connections, and user keyboard interrupts (`Ctrl+C`).

### Tools & Libraries Used
- **Language:** Python 3
- **Libraries:** `socket`, `sys`, `datetime` (Built-in standard libraries, requiring no external dependencies)
