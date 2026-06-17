import random
import math

def miller_rabin_test(n, k=10):
    """
    Miller-Rabin probabilistic primality test.
    
    Args:
        n: Number to test for primality
        k: Number of iterations (higher k = higher confidence)
    
    Returns:
        True if n is probably prime, False if n is composite
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as 2^r * d where d is odd
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Witness loop - perform k iterations
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)  # Modular exponentiation
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True


def generate_prime(bit_length):
    """
    Generate a random prime number with specified bit length using Miller-Rabin test.
    
    Args:
        bit_length: Number of bits in the prime number
    
    Returns:
        A prime number with approximately bit_length bits
    """
    while True:
        # Generate random odd number in the range
        num = random.getrandbits(bit_length)
        num |= (1 << bit_length - 1) | 1  # Set MSB and LSB to 1 (ensure bit_length bits and odd)
        
        if miller_rabin_test(num):
            return num


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    """
    Calculate the modular multiplicative inverse of e modulo phi.
    Uses the Extended Euclidean Algorithm.
    
    Args:
        e: The number to find inverse for
        phi: The modulus (phi(n))
    
    Returns:
        The modular inverse d such that (e * d) % phi == 1
    """
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd_val, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd_val, x, y
    
    _, x, _ = extended_gcd(e % phi, phi)
    return (x % phi + phi) % phi


def generate_keypair(bit_length=16):
    """
    Generate RSA public and private keys.
    
    Args:
        bit_length: Bit length for each prime number (smaller for demo, use 1024+ for security)
    
    Returns:
        Tuple of (public_key, private_key) where:
        - public_key = (n, e)
        - private_key = (n, d)
    """
    print(f"\n>>> Generating two {bit_length}-bit prime numbers using Miller-Rabin test...")
    
    # Generate two distinct random primes
    p = generate_prime(bit_length)
    q = generate_prime(bit_length)
    
    while p == q:
        q = generate_prime(bit_length)
    
    print(f"    Prime p: {p}")
    print(f"    Prime q: {q}")
    
    # Compute n = p * q
    n = p * q
    print(f"    Modulus n (p*q): {n}")
    
    # Compute Euler's totient function: phi(n) = (p-1) * (q-1)
    phi = (p - 1) * (q - 1)
    print(f"    Phi(n) = (p-1)*(q-1): {phi}")
    
    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    # Common choice: e = 65537, but for small primes, use smaller value
    e = 65537
    while e >= phi or gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    print(f"    Public exponent e: {e}")
    
    # Compute d, the modular multiplicative inverse of e modulo phi
    d = mod_inverse(e, phi)
    print(f"    Private exponent d: {d}")
    
    return (n, e), (n, d)


def encrypt(message, public_key):
    """
    Encrypt a message using the public key.
    
    Args:
        message: String message to encrypt
        public_key: Tuple (n, e)
    
    Returns:
        List of encrypted numbers (one per character)
    """
    n, e = public_key
    encrypted = []
    
    for char in message:
        # Convert character to ASCII value
        m = ord(char)
        # Encrypt using formula: c = m^e mod n
        c = pow(m, e, n)
        encrypted.append(c)
    
    return encrypted


def decrypt(encrypted_message, private_key):
    """
    Decrypt an encrypted message using the private key.
    
    Args:
        encrypted_message: List of encrypted numbers
        private_key: Tuple (n, d)
    
    Returns:
        Decrypted string message
    """
    n, d = private_key
    decrypted = []
    
    for c in encrypted_message:
        # Decrypt using formula: m = c^d mod n
        m = pow(c, d, n)
        # Convert number back to character
        decrypted.append(chr(m))
    
    return ''.join(decrypted)


def main():
    """Main function to demonstrate RSA encryption and decryption."""
    print("=" * 70)
    print(" " * 15 + "RSA Encryption and Decryption System")
    print("=" * 70)
    
    # Generate keypair (using 16-bit primes for demo - increase for security)
    print("\n[STEP 1: KEY GENERATION]")
    print("-" * 70)
    public_key, private_key = generate_keypair(bit_length=16)
    
    print("\n[STEP 2: DISPLAY GENERATED KEYS]")
    print("-" * 70)
    n, e = public_key
    _, d = private_key
    print(f"\n  Public Key (n, e):  ({n}, {e})")
    print(f"  Private Key (n, d): ({n}, {d})")
    
    # Get user input
    print("\n[STEP 3: MESSAGE ENCRYPTION]")
    print("-" * 70)
    message = input("\nEnter a message to encrypt (short message recommended): ")
    
    # Validate message
    if not message:
        print("No message entered. Using default: 'HELLO'")
        message = "HELLO"
    
    print(f"\n  Original Message: '{message}'")
    
    # Check if message characters are within valid range
    for char in message:
        if ord(char) >= n:
            print(f"\n  ⚠ WARNING: Character '{char}' (ASCII {ord(char)}) is >= n ({n})")
            print(f"  This will cause issues. Please use shorter messages or larger primes.")
            return
    
    # Encrypt the message
    encrypted = encrypt(message, public_key)
    print(f"\n  Encrypted Message (ciphertext):")
    print(f"  {encrypted}")
    
    # Decrypt the message
    print("\n[STEP 4: MESSAGE DECRYPTION]")
    print("-" * 70)
    decrypted = decrypt(encrypted, private_key)
    print(f"\n  Decrypted Message: '{decrypted}'")
    
    # Verification
    print("\n[VERIFICATION]")
    print("-" * 70)
    if message == decrypted:
        print("  ✓ SUCCESS: Decrypted message matches original message!")
    else:
        print("  ✗ FAILURE: Messages do not match!")
    
    print("\n" + "=" * 70)
    print("\nNOTE: This is a simplified demonstration using small primes (16-bit).")
    print("For production use, use larger primes (1024+ bits) for security.")
    print("=" * 70)


if __name__ == "__main__":
    main()
