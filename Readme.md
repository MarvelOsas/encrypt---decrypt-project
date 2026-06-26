# Custom Cryptographic Suites & Cipher Utilities

A comprehensive Python project demonstrating modern cryptography techniques including a tailored **Caesar Cipher**, asymmetric **RSA (Asymmetric Encryption)**, and branded **AES (Symmetric Encryption)**.

This project is perfect for beginners learning cybersecurity, cryptography fundamentals, and Python programming.

---

## 🛠️ Features

### ### 1. **Caesar Cipher** (`cipher.py`)
* ✓ Encrypt any text using a shift key
* ✓ Decrypt encrypted text back to original
* ✓ Preserves uppercase, lowercase, spaces, and punctuation
* ✓ Custom interactive console wrapper interface

### ### 2. **RSA Encryption** (`rsa_encryption.py`)
* ✓ Generates two random prime numbers using Miller-Rabin primality test
* ✓ Computes public key (n, e) and private key (n, d)
* ✓ Encrypts/decrypts messages using modular exponentiation
* ✓ Implements Extended Euclidean Algorithm for key generation
* ✓ Complete demonstration with user input

### ### 3. **AES Symmetric Encryption** (`aes_encryption.py`)
* ✓ Generates random AES keys or derives them from passwords
* ✓ Uses custom **PBKDF2** with a static salt architecture for seamless, predictable key derivation
* ✓ Uses AES-128 encryption in **CBC mode**
* ✓ HMAC authentication for message integrity
* ✓ Full encryption/decryption demonstration including dynamic file handling  

---

## 🧠 Understanding Encryption Methods

### Caesar Cipher
A substitution cipher where each letter is shifted by a fixed number.
- **Example**: HELLO with shift 3 → KHOOR
- **Use case**: Educational - demonstrates basic encryption concepts
- **Security**: NOT suitable for production (easily broken)

### RSA (Asymmetric Encryption)
Public-key cryptography using two different keys for encryption/decryption.
- **How it works**: 
  - Public key (n, e) encrypts messages
  - Private key (n, d) decrypts messages
  - Based on the difficulty of factoring large primes
- **Use case**: Secure communication, digital signatures
- **Security**: Strong when using large primes (1024+ bits)

### AES (Symmetric Encryption)
Secret-key cryptography using the same key for encryption/decryption.
- **How it works**:
  - One shared secret key encrypts and decrypts
  - Uses CBC mode for additional security
  - HMAC provides authenticity verification
- **Use case**: Fast encryption of large data
- **Security**: Very strong and widely used in production

---

## ▶️ How to Run the Programs

### Prerequisites
```bash
# For Caesar Cipher (no dependencies needed)
python cipher.py

# For RSA Encryption (no external dependencies)
python rsa_encryption.py

# For AES Encryption (requires cryptography library)
pip install cryptography
python aes_encryption.py
```

### Caesar Cipher Example
```
Input:
  Message: "Attack At Dawn"
  Shift: 3

Output:
  Encrypted: "Dwwdfn Dw Gdzq"
  Decrypted Back: "Attack At Dawn"
```

### RSA Encryption Example
```
[STEP 1: KEY GENERATION]
>>> Generating two 16-bit prime numbers using Miller-Rabin test...
    Prime p: 53261
    Prime q: 61829
    Modulus n (p*q): 3291475169
    Public exponent e: 17
    Private exponent d: 1935799577

[STEP 2: MESSAGE ENCRYPTION]
Enter a message: "HI"
    Encrypted Message: [1445897432, 373669173]

[STEP 3: MESSAGE DECRYPTION]
    Decrypted Message: "HI"
    ✓ SUCCESS: Decrypted message matches original!
```

### AES Encryption Example
```
[STEP 1: AES KEY GENERATION]
Generate key from:
  1. Random (secure)
  2. Password
Choose: 1
    Key (base64): gAAAAABmXxY5K8x...

[STEP 2: MESSAGE INPUT]
Enter a message: "Hello World"

[STEP 3: MESSAGE ENCRYPTION]
    Encrypted Message (ciphertext): b'gAAAAABmXxY5...'
    Ciphertext (base64): gAAAAABmXxY5K8x...

[STEP 4: MESSAGE DECRYPTION]
    Decrypted Message: "Hello World"
    ✓ SUCCESS: Decrypted message matches original!
```

---

## 📂 Project Structure

```
Encrypt---decrypt-project/
│
├── cipher.py              # Caesar Cipher implementation
├── rsa_encryption.py      # RSA encryption with Miller-Rabin test
├── aes_encryption.py      # AES-128 CBC mode encryption
└── Readme.md              # Project documentation
```

---

## 🔑 Key Algorithms Implemented

### 1. Miller-Rabin Primality Test
Used in RSA to generate large prime numbers with high confidence.
- Probabilistic algorithm (k iterations determine accuracy)
- Much faster than trial division
- Used in modern cryptography systems

### 2. Extended Euclidean Algorithm
Used in RSA to compute the private key (d) from public exponent (e).
- Finds modular multiplicative inverse
- Critical for RSA key generation

### 3. PBKDF2 (Password-Based Key Derivation Function)
Used in AES to derive encryption keys from passwords.
- Applies SHA-256 hashing 100,000 times
- Adds salt for resistance against rainbow table attacks
- Industry-standard key derivation method

---

## 🧪 Security Notes

⚠️ **Caesar Cipher**
- NOT secure - easily broken by brute force
- Educational purposes only

⚠️ **RSA (Demo Version)**
- Current implementation uses 16-bit primes for demo
- Production use requires 1024+ bit primes
- For demonstration/learning only

✅ **AES Encryption**
- Production-ready implementation
- AES-128 is cryptographically secure
- HMAC provides authenticity

---

## 🤝 Contributing

This is an educational project — feel free to:
- Fork it and improve it
- Add more encryption algorithms
- Optimize the implementations
- Open pull requests with enhancements

---

## 📚 Resources

- [RSA Cryptography](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [AES Encryption](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [Python Cryptography Library](https://cryptography.io/)
- [Miller-Rabin Test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)

---


This project is open source and available for educational purposes.

