# What is HTML Smuggling?
- HTML smuggling is a technique used to bypass security defenses by embedding a Base64-encoded file inside an HTML page. When executed in a browser, JavaScript reconstructs and downloads the file on the client-side, avoiding detection by network security systems.

## How It Works
- A malicious file (e.g., an EXE) is Base64-encoded and embedded in an HTML file.
- When the victim opens the HTML file, JavaScript decodes the Base64 data.
- The script converts the data into a blob object and creates a download link dynamically.
- The file is then downloaded and executed on the victim’s machine if they interact with it.
