import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    
    except FileNotFoundError:
        print("File not found!")
        return None


def save_hash(file_path, hash_value):
    with open("hash_store.txt", "w") as f:
        f.write(f"{file_path}|{hash_value}")


def check_integrity(file_path):
    if not os.path.exists("hash_store.txt"):
        print("No stored hash found.")
        return

    with open("hash_store.txt", "r") as f:
        stored_file, stored_hash = f.read().split("|")

    current_hash = calculate_hash(file_path)

    if current_hash == stored_hash:
        print("✅ File integrity maintained. No changes detected.")
    else:
        print("❌ File integrity violated! File has been modified.")


# -------- MAIN PROGRAM --------
print("1. Generate Hash")
print("2. Check File Integrity")

choice = input("Enter your choice (1/2): ")
file_path = input("Enter file path: ")

if choice == "1":
    hash_value = calculate_hash(file_path)
    if hash_value:
        save_hash(file_path, hash_value)
        print("Hash generated and saved successfully.")
        print("Hash:", hash_value)

elif choice == "2":
    check_integrity(file_path)

else:
    print("Invalid choice!")
