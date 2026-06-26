def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char  # leave spaces and punctuation unchanged

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("::: Marvel's Custom Caesar Cipher Tool :::")
    print("-----------------------------------------")
    
    message = input("Enter your message: ")
    
    # Dynamic user input validation for the shift key
    try:
        shift = int(input("Enter a secret shift key number (1-25): "))
        if not (1 <= shift <= 25):
            print("Out of range. Defaulting shift key to 3.")
            shift = 3
    except ValueError:
        print("Invalid number format. Defaulting shift key to 3.")
        shift = 3

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print("\n--- Results ---")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted Back: {decrypted}")


if __name__ == "__main__":
    main()
# Caesar Cipher Implementation