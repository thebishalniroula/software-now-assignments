# Question 1
# Create a program that reads the text file "raw_text.txt", encrypts its contents using a
# simple encryption method, and writes the encrypted text to a new file
# "encrypted_text.txt". Then create a function to decrypt the content and a function to
# verify the decryption was successful.
# Requirements
# The encryption should take two user inputs (shift1, shift2), and follow these rules:
# • For lowercase letters:
# o If the letter is in the first half of the alphabet (a-m): shift forward by shift1 *
# shift2 positions
# o If the letter is in the second half (n-z): shift backward by shift1 + shift2
# positions
# • For uppercase letters:
# o If the letter is in the first half (A-M): shift backward by shift1 positions
# o If the letter is in the second half (N-Z): shift forward by shift2² positions
# (shift2 squared)
# • Other characters:
# o Spaces, tabs, newlines, special characters, and numbers remain
# unchanged
# Main Functions to Implement
# Encryption function: Reads from "raw_text.txt" and writes encrypted content to
# "encrypted_text.txt" .
# Decryption function: Reads from "encrypted_text.txt" and writes the decrypted
# content to "decrypted_text.txt" .
# Verification function: Compares "raw_text.txt" with "decrypted_text.txt" and prints
# whether the decryption was successful or not.
# Program Behavior
# When run, your program should automatically:
# 1. 2. 4. Prompt the user for shift1 and shift2 values
# Encrypt the contents of "raw_text.txt"
# 3. Decrypt the encrypted file
# Verify the decryption matches the original


file_path = "raw_text.txt"

def encrypt_char(c, shift1, shift2):
        if 'a' <= c <= 'm':
            unicode_for_a = ord('a')
            shift_value = shift1 * shift2
            character_index = ord(c) - unicode_for_a
            encrypted_index = (character_index + shift_value) % 26
            return chr(encrypted_index + unicode_for_a)
        elif 'n' <= c <= 'z':
            unicode_for_a = ord('a')
            shift_value = shift1 + shift2
            character_index = ord(c) - unicode_for_a
            encrypted_index = (character_index - shift_value) % 26
            return chr(encrypted_index + unicode_for_a)
        elif 'A' <= c <= 'M':
            unicode_for_A = ord('A')
            shift_value = shift1
            character_index = ord(c) - unicode_for_A
            encrypted_index = (character_index - shift_value) % 26
            return chr(encrypted_index + unicode_for_A)
        elif 'N' <= c <= 'Z':
            unicode_for_A = ord('A')
            shift_value = shift2 ** 2
            character_index = ord(c) - unicode_for_A
            encrypted_index = (character_index + shift_value) % 26
            return chr(encrypted_index + unicode_for_A)
        else:
            return c
        
def encrypt_text(content, shift1, shift2):
    encrypted_content = ""
    for c in content:
        encrypted_content += encrypt_char(c, shift1, shift2)
    return encrypted_content

def decrypt_char(c, shift1, shift2):
        if 'a' <= c <= 'm':
            unicode_for_a = ord('a')
            shift_value = shift1 * shift2
            character_index = ord(c) - unicode_for_a
            decrypted_index = (character_index - shift_value) % 26
            return chr(decrypted_index + unicode_for_a)
        elif 'n' <= c <= 'z':
            unicode_for_a = ord('a')
            shift_value = shift1 + shift2
            character_index = ord(c) - unicode_for_a
            decrypted_index = (character_index + shift_value) % 26
            return chr(decrypted_index + unicode_for_a)
        elif 'A' <= c <= 'M':
            unicode_for_A = ord('A')
            shift_value = shift1
            character_index = ord(c) - unicode_for_A
            decrypted_index = (character_index + shift_value) % 26
            return chr(decrypted_index + unicode_for_A)
        elif 'N' <= c <= 'Z':
            unicode_for_A = ord('A')
            shift_value = shift2 ** 2
            character_index = ord(c) - unicode_for_A
            decrypted_index = (character_index - shift_value) % 26
            return chr(decrypted_index + unicode_for_A)
        else:
            return c

def decrypt_text(encrypted_content, shift1, shift2):
    decrypted_content = ""
    for c in encrypted_content:
        decrypted_content += decrypt_char(c, shift1, shift2)
    write_file("decrypted_text.txt", decrypted_content)
    return decrypted_content
        
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def read_shift_values():
    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))
    return shift1, shift2


def verify_decryption(original_file, decrypted_file):
    original_content = read_file(original_file)
    decrypted_content = read_file(decrypted_file)
    if original_content == decrypted_content:
        return True
    else:
        return False
        
def main():
    shift1, shift2 = read_shift_values()
    raw_file_text = read_file(file_path)

    encrypted_content = encrypt_text(raw_file_text, shift1, shift2)
    write_file("encrypted_text.txt", encrypted_content)

    encrypted_file_text = read_file("encrypted_text.txt")
    decrypted_content = decrypt_text(encrypted_file_text, shift1, shift2)

    verify_success = verify_decryption(file_path, "decrypted_text.txt")

    if verify_success:
        print("Decryption successful: The decrypted text matches the original.")
    else:
        print("Decryption failed: The decrypted text does not match the original.")

    verify_success = decrypt_text(encrypted_file_text, shift1, shift2)

    
main()