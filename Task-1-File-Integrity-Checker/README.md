# 🔐 Task 1 – File Integrity Checker

## 📌 Project Overview

The File Integrity Checker is a Python-based security tool developed as part of the CODTECH Cyber Security Internship.

This tool monitors changes in files by calculating and comparing cryptographic hash values. If a file is modified, its hash value changes, allowing detection of tampering.

---

## 🎯 Objective

The objective of this task is to:

- Calculate the hash value of a file
- Store the original hash value
- Compare hash values during verification
- Detect any modification in the file
- Ensure file integrity using cryptographic techniques

---

## 🛠 Technologies Used

- Python
- hashlib (Built-in Python Library)
- File Handling

---

## 🔍 How It Works

1. The program reads the selected file in binary mode.
2. It generates a SHA-256 hash value.
3. The original hash is stored or displayed.
4. When the file is checked again, a new hash is generated.
5. If both hash values match → File is secure.
6. If hash values differ → File has been modified.

---

## 📂 Project Structure

Task-1-File-Integrity-Checker/
│
├── file_integrity_checker.py
├── sample_file.txt
└── README.md

---

## ▶️ How to Run the Program

1. Open Command Prompt or Terminal.
2. Navigate to the project folder:

   cd Task-1-File-Integrity-Checker

3. Run the script:

   python file_integrity_checker.py

4. Enter the file name when prompted.

---

## 🧪 Example Output

Example 1 (File Not Modified):

Enter file name: sample_file.txt  
Original Hash: 9f86d081884c7d659a2feaa0c55ad015...  
File is secure. No changes detected.

Example 2 (File Modified):

Warning! File has been modified.

---

## 🔐 Importance of File Integrity

File integrity checking is important in cybersecurity because it helps:

- Detect unauthorized changes
- Prevent malware tampering
- Protect sensitive data
- Maintain system security
 

---

## ⚠️ Disclaimer

This project is developed for educational and internship purposes only.  
The tool should be used responsibly and ethically.    
