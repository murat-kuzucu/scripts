# What is HTML Smuggling?
- HTML smuggling is a technique used to bypass security defenses by embedding a Base64-encoded file inside an HTML page. When executed in a browser, JavaScript reconstructs and downloads the file on the client-side, avoiding detection by network security systems.

## How It Works
- A malicious file (e.g., an EXE) is Base64-encoded and embedded in an HTML file.
- When the victim opens the HTML file, JavaScript decodes the Base64 data.
- The script converts the data into a blob object and creates a download link dynamically.
- The file is then downloaded and executed on the victim’s machine if they interact with it.

# SMTP Payload Sender
A simple SMTP tool for sending payload attachments during penetration testing.

## How It Works
Run:
```bash
python3 smtp-sender.py
```
## Usage Example
```bash
=== Email Configuration ===
Sender Email: admin@target.com
Target Email: user@target.com
Email Subject: Security Update Required

Email Content: 
Please install this critical security update.
[Press Enter twice to finish]

Payload file path: /path/to/payload.exe
Fake filename: security_update.exe

=== SMTP Server Configuration ===
SMTP Server: mail.target.com
SMTP Port [25]: 25
```
# Hex Converter for /proc/net/tcp

Python utilities for converting hex values from `/proc/net/tcp` to readable IP addresses.

## Files

**hexconverter-for-proc-net-tcp.py**
- Enter hex value → get IP address

**dumped-proc-net-tcp.py**  
- Paste `/proc/net/tcp` content → get formatted connections

## Usage

Run script, enter/paste data, get converted output.
