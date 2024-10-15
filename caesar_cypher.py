# Caesar Cipher Program (Interactive)

def encrypt_caesar_cipher(plain_text, shift):
    encrypted_text = ""
    
    for char in plain_text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
            
    return encrypted_text

def decrypt_caesar_cipher(encrypted_text, shift):
    decrypted_text = ""
    
    for char in encrypted_text:
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
            
    return decrypted_text

# Interactive Caesar Cipher Program

def caesar_cipher():
    action = input("Do you want to Encrypt or Decrypt the message? (E/D): ").upper()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (an integer): "))

    if action == 'E':
        result = encrypt_caesar_cipher(message, shift)
        print("\nEncrypted Message:", result)
    elif action == 'D':
        result = decrypt_caesar_cipher(message, shift)
        print("\nDecrypted Message:", result)
    else:
        print("Invalid option! Please select 'E' for Encryption or 'D' for Decryption.")

# Call the interactive function
caesar_cipher()
