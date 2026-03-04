import socket
import time

# ---------------- PORT SCANNER ----------------
def port_scanner():
    target = input("Enter target IP address: ")
    print(f"\nScanning ports on {target}...\n")

    for port in range(20, 1025):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            sock.close()
        except:
            pass

    print("\nPort scanning completed.\n")

# ---------------- BRUTE FORCE DEMO ----------------
def brute_force_demo():
    username = input("Enter username: ")
    password_list = ["1234", "admin", "password", "admin123", "root"]

    print("\nStarting brute force simulation...\n")
    for pwd in password_list:
        print(f"Trying password: {pwd}")
        time.sleep(0.5)

        # Dummy condition for demo
        if pwd == "admin123":
            print(f"\n[✓] Password found: {pwd}")
            return

    print("\n[✗] Password not found.")

# ---------------- MAIN MENU ----------------
def main():
    while True:
        print("==== PENETRATION TESTING TOOLKIT ====")
        print("1. Port Scanner")
        print("2. Brute Force Demo")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            port_scanner()
        elif choice == "2":
            brute_force_demo()
        elif choice == "3":
            print("Exiting toolkit.")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
