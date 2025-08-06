# Secure Authentication (Password Strength Checker)

## Overview

This is a simple command-line program written in Python that performs two essential security checks on a user-inputted password:

1. **Password Strength Check** using entropy calculation.
2. **Leaked Password Detection** using a simulated **Bloom filter** and a list of leaked passwords.

The goal of this project is to demonstrate the basics of password security, entropy evaluation, and the application of Bloom filters in a system security context.

---

## Features

- Calculates **password entropy** based on the character sets used.
- Warns the user if the password's entropy is **below the minimum threshold** (30 bits).
- Checks if the password **may have been leaked** using a **Bloom filter**.
- Provides **security tips** if the password is weak.
- Uses a simulated list of leaked passwords (`LeakedPwd`).

---

## Requirements

- Python 3.6 or higher
- No external libraries required — uses only Python standard libraries (`math`, `hashlib`).

---

## How to Run

1. **Download or clone the repository.**

2. Open a terminal or command prompt in the project directory.

3. Run the script using:

   ```bash
   python password_checker.py
   ```

4. Follow the on-screen prompt to enter a new password.

---

## What to Expect

- The program will:
  - Display the **calculated entropy** of the entered password.
  - Warn you if the entropy is too low (below 30 bits in this case).
  - Suggest improvements for stronger password creation.
  - Let you know if the password may have been part of a known data leak (based on the simulated list).

---

## Example Output

```bash
Enter a new password: pass123

Password Entropy: 37.86 bits
Password entropy is sufficient.

Warning: This password may have been leaked before!
```

---

## Notes

- The **Bloom filter** is implemented from scratch using:
  - A fixed-size bit array (default: 500 bits).
  - 3 simple hash functions (based on MD5 with different seeds).

- The list of leaked passwords is simulated using this array:
  ```python
  LeakedPwd = ["password123", "123", "123456", "qwerty", "letmein", "admin"]
  ```

- The entropy formula used is:
  \[
  	Entropy = L x log2(N)
  \]
  
  where:
  - \(L\) = length of the password
  - \(N\) = size of the character set used (e.g., lowercase, digits, symbols)

---

## Author

This project was developed as part of the **System Security** course for Spring 2025.

---

## License

This code is provided for educational purposes. You are free to modify and reuse it for non-commercial use.
