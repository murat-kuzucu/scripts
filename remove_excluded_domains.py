#!/usr/bin/env python3

def load_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def is_excluded(domain, excluded_domains):
    for excluded in excluded_domains:
        if domain == excluded:
            return True
        
        if excluded.startswith('*.'):
            base_domain = excluded[2:]
            if domain.endswith('.' + base_domain) or domain == base_domain:
                return True
    
    return False

def filter_domains(subdomains, excluded_domains):
    filtered = []
    excluded_count = 0
    
    for subdomain in subdomains:
        if not is_excluded(subdomain, excluded_domains):
            filtered.append(subdomain)
        else:
            excluded_count += 1
    
    print(f"Total subdomains: {len(subdomains)}")
    print(f"Excluded: {excluded_count}")
    print(f"Remaining: {len(filtered)}")
    
    return filtered

def save_file(filename, domains):
    with open(filename, 'w', encoding='utf-8') as f:
        for domain in domains:
            f.write(domain + '\n')
    print(f"\nFiltered results saved to '{filename}'")

def main():
    excluded_file = 'excluded-domains.txt'
    subdomains_file = 'subdomains-dns.txt'
    output_file = 'filtered-subdomains.txt'
    
    print("Loading files...")
    excluded_domains = load_file(excluded_file)
    subdomains = load_file(subdomains_file)
    
    if not excluded_domains:
        print("Warning: No excluded domains found.")
    if not subdomains:
        print("Error: No subdomains found.")
        return
    
    print(f"Loaded {len(excluded_domains)} excluded domains")
    print(f"Loaded {len(subdomains)} subdomains")
    print("\nFiltering...")
    
    filtered_subdomains = filter_domains(subdomains, excluded_domains)
    
    save_file(output_file, filtered_subdomains)

if __name__ == '__main__':
    main()
