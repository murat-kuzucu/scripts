#!/usr/bin/env python

def read_names_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def generate_ad_usernames(fullName):
    parts = fullName.split()
    
    if len(parts) == 1:
        return {
            "single_name": parts[0].lower(),
        }
    
    firstName = parts[0]
    lastName = parts[-1]
    
    usernames = {
        "first_initial_last": f"{firstName[0].lower()}{lastName.lower()}",
        "first_last": f"{firstName.lower()}{lastName.lower()}",
        "first_dot_last": f"{firstName.lower()}.{lastName.lower()}",
        "first_underscore_last": f"{firstName.lower()}_{lastName.lower()}",
        "last_first_initial": f"{lastName.lower()}{firstName[0].lower()}",
        "last_dot_first": f"{lastName.lower()}.{firstName.lower()}",
    }
    
    if len(parts) > 2:
        middleInitial = parts[1][0].lower()
        usernames["first_middle_initial_last"] = f"{firstName.lower()}{middleInitial}{lastName.lower()}"
        usernames["first_initial_middle_initial_last"] = f"{firstName[0].lower()}{middleInitial}{lastName.lower()}"
    
    return usernames

def main():
    inputFilePath = "user.txt"
    outputFilePath = "ad-user.txt"
    names = read_names_from_file(inputFilePath)
    
    if not names:
        print("No names found to process.")
        return
    
    print(f"Found {len(names)} names in {inputFilePath}")
    print(f"Exporting usernames to {outputFilePath}...")
    
    try:
        with open(outputFilePath, 'w') as outputFile:
            for name in names:
                usernames = generate_ad_usernames(name)
                for _, username in usernames.items():
                    outputFile.write(f"{username}\n")
        
        print(f"Successfully exported usernames to {outputFilePath}")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()
