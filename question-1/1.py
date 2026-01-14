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


RAW_FILE_PATH = "raw_text.txt"
ENCRYPTED_FILE_PATH = "encrypted_text.txt"
DECRYPTED_FILE_PATH = "decrypted_text.txt"

def create_character_map(shift1, shift2):
    encrypt_map = {}
    
    # Calculate shifts
    lower_forward_shift = (shift1 * shift2) % 26  # for a-m
    lower_backward_shift = (shift1 + shift2) % 26  # for n-z
    upper_backward_shift = shift1 % 26  # for A-M
    upper_forward_shift = (shift2 ** 2) % 26  # for N-Z
    
    # For lowercase letters
    for i in range(26):
        ch = chr(ord('a') + i)
        
        if 'a' <= ch <= 'm':  # First half of lowercase alphabet
            new_pos = (i + lower_forward_shift) % 26
            encrypt_map[ch] = chr(ord('a') + new_pos)
        else:  # Second half
            new_pos = (i - lower_backward_shift) % 26
            encrypt_map[ch] = chr(ord('a') + new_pos)
    
    # For uppercase letters
    for i in range(26):
        ch = chr(ord('A') + i)
        
        if 'A' <= ch <= 'M':  # First half of uppercase alphabet
            new_pos = (i - upper_backward_shift) % 26
            encrypt_map[ch] = chr(ord('A') + new_pos)
        else:  # Second half
            new_pos = (i + upper_forward_shift) % 26
            encrypt_map[ch] = chr(ord('A') + new_pos)
    
    # Decryption map is the inverse of encryption map
    decrypt_map = {v: k for k, v in encrypt_map.items()}
    
    return encrypt_map, decrypt_map

print(create_character_map(1, 2))
        
# def encrypt_text(content, shift1, shift2):
#     encrypt_map, _ = create_character_map(shift1, shift2)
#     encrypted_content = ""
#     for c in content:
#         # If character is not an alphabetic character, leave it unchanged
#         if c not in encrypt_map:
#             encrypted_content += c
#         else:
#             encrypted_content += encrypt_map[c]
#     return encrypted_content


# def decrypt_text(encrypted_content, shift1, shift2):
#     _, decrypt_map = create_character_map(shift1, shift2)
#     decrypted_content = ""
#     for c in encrypted_content:
#         # If character is not an alphabetic character, leave it unchanged
#         if c not in decrypt_map:
#             decrypted_content += c
#         else:
#             decrypted_content += decrypt_map[c]
#     return decrypted_content
        
# def read_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return file.read()
    
# def write_file(file_path, content):
#     with open(file_path, 'w', encoding='utf-8') as file:
#         file.write(content)


# def read_shift_values():
#     shift1 = int(input("Enter shift1 value: "))
#     shift2 = int(input("Enter shift2 value: "))
#     return shift1, shift2


# def verify_decryption(original_file, decrypted_file):
#     original_content = read_file(original_file)
#     decrypted_content = read_file(decrypted_file)
#     if original_content == decrypted_content:
#         return True
#     else:
#         return False
        
# def main():
#     shift1, shift2 = read_shift_values()
#     raw_file_text = read_file(RAW_FILE_PATH)

#     # Encrypt
#     encrypted_content = encrypt_text(raw_file_text, shift1, shift2)
#     write_file(ENCRYPTED_FILE_PATH, encrypted_content)

#     # Decrypt
#     encrypted_file_text = read_file(ENCRYPTED_FILE_PATH)
#     decrypted_content = decrypt_text(encrypted_file_text, shift1, shift2)
#     write_file(DECRYPTED_FILE_PATH, decrypted_content)

#     # Verify
#     verify_success = verify_decryption(RAW_FILE_PATH, DECRYPTED_FILE_PATH)

#     if verify_success:
#         print("Decryption successful: The decrypted text matches the original.")
#     else:
#         print("Decryption failed: The decrypted text does not match the original.")


# main()