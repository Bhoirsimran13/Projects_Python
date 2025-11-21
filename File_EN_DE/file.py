# encrypt text using Caesar Cipher
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def encrypt_file(filename, shift):
    with open(filename, "r") as file:
        content = file.read()
    
    encrypted_content = caesar_encrypt(content, shift)
    
    with open(filename + ".encrypted", "w") as enc_file:
        enc_file.write(encrypted_content)
    
    print(f"File '{filename}' encrypted successfully!")

def decrypt_file(filename, shift):
    with open(filename, "r") as enc_file:
        content = enc_file.read()
    
    decrypted_content = caesar_decrypt(content, shift)
    
    new_filename = filename.replace(".encrypted", "_decrypted.txt")
    with open(new_filename, "w") as dec_file:
        dec_file.write(decrypted_content)
    
    print(f"File '{filename}' decrypted successfully as '{new_filename}'!")

if __name__ == "__main__":
    print("1. Encrypt File")
    print("2. Decrypt File")
    choice = input("Enter choice (1/2): ")

    filename = input("Enter file name: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    if choice == "1":
        encrypt_file(filename, shift)
    elif choice == "2":
        decrypt_file(filename, shift)
    else:
        print("Invalid choice!")
