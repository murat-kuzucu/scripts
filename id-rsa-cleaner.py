import re
import os
import sys
from pathlib import Path


def is_valid_line(line):
    line = line.strip()
    if not line or line.startswith(('#', '//', '/*')):
        return False
    
    dummy_words = ['dummy', 'test', 'sample', 'placeholder', 'example', 'fake']
    if any(word in line.lower() for word in dummy_words):
        return False
    
    return re.match(r'^[A-Za-z0-9+/=\s]+$', line) is not None


def extract_key(content):
    lines = content.split('\n')
    result = []
    in_key = False
    
    begin_markers = ['BEGIN RSA PRIVATE KEY', 'BEGIN OPENSSH PRIVATE KEY', 'BEGIN PRIVATE KEY']
    end_markers = ['END RSA PRIVATE KEY', 'END OPENSSH PRIVATE KEY', 'END PRIVATE KEY']
    
    for line in lines:
        line = line.strip()
        
        if not in_key and any(marker in line for marker in begin_markers):
            in_key = True
            result.append(line)
        elif in_key and any(marker in line for marker in end_markers):
            result.append(line)
            break
        elif in_key and is_valid_line(line):
            result.append(line)
    
    return '\n'.join(result)


def clean_file(input_file):
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_file}")
    
    output_file = input_path.parent / "cleaned-id-rsa"
    
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    cleaned = extract_key(content)
    if not cleaned.strip():
        raise ValueError("No valid SSH key found")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    
    return str(output_file)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python id-rsa-cleaner.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    try:
        result = clean_file(input_file)
        print(f"Cleaned key saved to: {result}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
