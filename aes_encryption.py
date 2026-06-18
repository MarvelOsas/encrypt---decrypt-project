"""
AES Symmetric Encryption and Decryption
Implements AES-128 encryption in CBC mode using the cryptography library.

Installation:
    pip install cryptography
"""

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os
import base64


def generate_aes_key():
    """
    Generate a random AES key (Fernet uses AES-128 in CBC mode).
    
    Returns:
        A URL-safe base64 encoded 32-byte key
    """
    return Fernet.generate_key()


def generate_key_from_password(password, salt=None):
    """
    Derive an AES key from a password using PBKDF2.
    
    Args:
        password: String password to derive key from
        salt: Optional salt (if None, a random salt is generated)
    
    Returns:
        Tuple of (key, salt) where key is URL-safe base64 encoded
    """
    if salt is None:
        salt = os.urandom(16)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt


def encrypt_message(message, key):
    """
    Encrypt a plaintext message using AES-128 CBC mode.
    
    Args:
        message: String message to encrypt
        key: Fernet key (32-byte URL-safe base64 encoded)
    
    Returns:
        Encrypted message (ciphertext) as bytes
    """
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    return encrypted


def decrypt_message(encrypted_message, key):
    """
    Decrypt an encrypted message using AES-128 CBC mode.
    
    Args:
        encrypted_message: Encrypted message (ciphertext) as bytes
        key: Fernet key (32-byte URL-safe base64 encoded)
    
    Returns:
        Decrypted plaintext message as string
    """
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_message)
    return decrypted.decode()


def main():
    """Main function to demonstrate AES encryption and decryption."""
    print("=" * 70)
    print(" " * 20 + "AES Symmetric Encryption System")
    print("=" * 70)
    
    # Step 1: Key Generation
    print("\n[STEP 1: AES KEY GENERATION]")
    print("-" * 70)
    
    choice = input("\nGenerate key from:\n  1. Random (secure)\n  2. Password\nChoose (1 or 2): ").strip()
    
    if choice == "2":
        # Generate key from password
        password = input("Enter a password: ")
        print("\n>>> Deriving AES key from password using PBKDF2...")
        key, salt = generate_key_from_password(password)
        print(f"    Salt (hex): {salt.hex()}")
        print(f"    Key (base64): {key.decode()}")
    else:
        # Generate random key
        print("\n>>> Generating random AES key...")
        key = generate_aes_key()
        salt = None
        print(f"    Key (base64): {key.decode()}")
    
    # Step 2: Get User Input
    print("\n[STEP 2: MESSAGE INPUT]")
    print("-" * 70)
    message = input("\nEnter a message to encrypt: ")
    
    if not message:
        print("No message entered. Using default: 'Hello, this is a secret message!'")
        message = "Hello, this is a secret message!"
    
    print(f"\n  Original Message: '{message}'")
    
    # Step 3: Encrypt Message
    print("\n[STEP 3: MESSAGE ENCRYPTION]")
    print("-" * 70)
    print("\n>>> Encrypting message using AES-128 CBC mode...")
    encrypted = encrypt_message(message, key)
    print(f"    Encrypted Message (ciphertext):")
    print(f"    {encrypted}")
    print(f"\n    Ciphertext (hex): {encrypted.hex()}")
    print(f"    Ciphertext (base64): {base64.b64encode(encrypted).decode()}")
    
    # Step 4: Decrypt Message
    print("\n[STEP 4: MESSAGE DECRYPTION]")
    print("-" * 70)
    print("\n>>> Decrypting message using AES-128 CBC mode...")
    decrypted = decrypt_message(encrypted, key)
    print(f"    Decrypted Message: '{decrypted}'")
    
    # Step 5: Verification
    print("\n[VERIFICATION]")
    print("-" * 70)
    if message == decrypted:
        print("  ✓ SUCCESS: Decrypted message matches original message!")
    else:
        print("  ✗ FAILURE: Messages do not match!")
    
    # Summary
    print("\n[SUMMARY]")
    print("-" * 70)
    print(f"  Original Length:   {len(message)} characters")
    print(f"  Encrypted Length:  {len(encrypted)} bytes")
    print(f"  Encryption Method: AES-128 CBC (via Fernet)")
    
    print("\n" + "=" * 70)
    print("\nNOTE: Fernet uses AES-128 in CBC mode with HMAC authentication.")
    print("This provides both confidentiality and authenticity.")
    print("=" * 70)


if __name__ == "__main__":
    main()
