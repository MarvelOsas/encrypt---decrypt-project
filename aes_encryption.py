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
        salt = b'MarvelsSecureSalt'
    
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

def encrypt_file(file_path, fernet_obj):
    import os
    if not os.path.exists(file_path):
        print("❌ Error: That file does not exist!")
        return
    with open(file_path, 'rb') as f:
        file_data = f.read()
    encrypted_data = fernet_obj.encrypt(file_data)
    output_path = file_path + ".enc"
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)
    print(f"\n🔒 Success! Encrypted file saved as: {output_path}")

def decrypt_file(file_path, fernet_obj):
    import os
    if not os.path.exists(file_path):
        print("❌ Error: That file does not exist!")
        return
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    try:
        decrypted_data = fernet_obj.decrypt(encrypted_data)
        output_path = file_path.replace(".enc", "") if file_path.endswith(".enc") else file_path + "_decrypted.txt"
        with open(output_path, 'wb') as f:
            f.write(decrypted_data)
        print(f"\n🔓 Success! Decrypted file restored to: {output_path}")
    except Exception:
        print("❌ Error: Decryption failed. Invalid key or corrupted data.")

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
    
    # This initializes the secure Fernet engine using the generated/derived key
    from cryptography.fernet import Fernet
    fernet = Fernet(key)

    # NEW UPGRADE: Operational Mode Menu
    print("\n" + "="*40)
    print("::: Choose Operation Mode :::")
    print("1. Encrypt Text Message")
    print("2. Decrypt Text Message")
    print("3. Encrypt an Entire File")
    print("4. Decrypt an Entire File")
    print("="*40)
    mode_choice = input("Select an option (1-4): ").strip()

    if mode_choice == "1":
        message = input("\nEnter the secret text message: ")
        encrypted = fernet.encrypt(message.encode())
        print(f"\n🔑 Ciphertext (Base64): {encrypted.decode()}")
        
    elif mode_choice == "2":
        ciphertext = input("\nEnter the Base64 encrypted text string: ").strip()
        try:
            decrypted = fernet.decrypt(ciphertext.encode())
            print(f"\n🔓 Decrypted Message: {decrypted.decode()}")
        except Exception:
            print("❌ Decryption failed. Invalid key or string.")
            
    elif mode_choice == "3":
        path = input("\nEnter the path to the file you want to encrypt (e.g., sample.txt): ").strip()
        encrypt_file(path, fernet)
        
    elif mode_choice == "4":
        path = input("\nEnter the path to the .enc file you want to decrypt: ").strip()
        decrypt_file(path, fernet)
    else:
        print("❌ Invalid mode selection.")
if __name__ == "__main__":
    main()
