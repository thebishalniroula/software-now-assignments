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

# Function to encrypt raw text
def encrypt_text(content, shift1, shift2):
    encrypted_content = ""
    
    # Calculate shifts based on rules
    lower_forward_shift = (shift1 * shift2) % 26  # for a-m
    lower_backward_shift = (shift1 + shift2) % 26  # for n-z
    upper_backward_shift = shift1 % 26  # for A-M
    upper_forward_shift = (shift2 ** 2) % 26  # for N-Z
    
    for char in content:
        if 'a' <= char <= 'z':  # Lowercase
            if 'a' <= char <= 'm':  # First half (a-m)
                # Shift forward by shift1 * shift2
                new_pos = (ord(char) - ord('a') + lower_forward_shift) % 26
                encrypted_char = chr(ord('a') + new_pos)
                # Add marker to indicate this was originally in first half
                encrypted_content += 'F' + encrypted_char
            else:  # Second half (n-z)
                # Shift backward by shift1 + shift2
                new_pos = (ord(char) - ord('a') - lower_backward_shift) % 26
                encrypted_char = chr(ord('a') + new_pos)
                encrypted_content += encrypted_char  # No marker for second half
                
        elif 'A' <= char <= 'Z':  # Uppercase
            if 'A' <= char <= 'M':  # First half (A-M)
                # Shift backward by shift1
                new_pos = (ord(char) - ord('A') - upper_backward_shift) % 26
                encrypted_char = chr(ord('A') + new_pos)
                # Add marker to indicate this was originally in first half
                encrypted_content += 'F' + encrypted_char
            else:  # Second half (N-Z)
                # Shift forward by shift2²
                new_pos = (ord(char) - ord('A') + upper_forward_shift) % 26
                encrypted_char = chr(ord('A') + new_pos)
                encrypted_content += encrypted_char  # No marker for second half
                
        else:  # Non-alphabetic characters
            encrypted_content += char
    
    return encrypted_content

# Function to decrypt encrypted text
def decrypt_text(encrypted_content, shift1, shift2):
    decrypted_content = ""
    i = 0
    
    # Calculate shifts (same as in encryption)
    lower_forward_shift = (shift1 * shift2) % 26
    lower_backward_shift = (shift1 + shift2) % 26
    upper_backward_shift = shift1 % 26
    upper_forward_shift = (shift2 ** 2) % 26
    
    while i < len(encrypted_content):
        char = encrypted_content[i]
        
        # Check for marker 'F' which indicates original was in first half
        if char == 'F' and i + 1 < len(encrypted_content):
            next_char = encrypted_content[i + 1]
            
            if 'a' <= next_char <= 'z':
                # Lowercase, was in first half (a-m): reverse forward shift
                new_pos = (ord(next_char) - ord('a') - lower_forward_shift) % 26
                decrypted_char = chr(ord('a') + new_pos)
                decrypted_content += decrypted_char
                i += 2  # Skip marker and character
                
            elif 'A' <= next_char <= 'Z':
                # Uppercase, was in first half (A-M): reverse backward shift
                new_pos = (ord(next_char) - ord('A') + upper_backward_shift) % 26
                decrypted_char = chr(ord('A') + new_pos)
                decrypted_content += decrypted_char
                i += 2  # Skip marker and character
                
            else:
                # Not a letter after marker, just add the 'F'
                decrypted_content += char
                i += 1
                
        elif 'a' <= char <= 'z':  # Lowercase without marker (was in second half)
            # Reverse backward shift
            new_pos = (ord(char) - ord('a') + lower_backward_shift) % 26
            decrypted_char = chr(ord('a') + new_pos)
            decrypted_content += decrypted_char
            i += 1
            
        elif 'A' <= char <= 'Z':  # Uppercase without marker (was in second half)
            # Reverse forward shift
            new_pos = (ord(char) - ord('A') - upper_forward_shift) % 26
            decrypted_char = chr(ord('A') + new_pos)
            decrypted_content += decrypted_char
            i += 1
            
        else:  # Non-alphabetic characters
            decrypted_content += char
            i += 1
    
    return decrypted_content

# Utility functions for file operations and verification
def read_file(file_path):
    """Read content from a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return ""

def write_file(file_path, content):
    """Write content to a file"""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Utility function for user input (shift values)
def read_shift_values():
    """Read shift values from user input"""
    while True:
        try:
            shift1 = int(input("Enter shift1 value (integer): "))
            shift2 = int(input("Enter shift2 value (integer): "))
            return shift1, shift2
        except ValueError:
            print("Please enter valid integers.")

# Utility function for verification
def verify_decryption(original_file, decrypted_file):
    original_content = read_file(original_file)
    decrypted_content = read_file(decrypted_file)
    
    if original_content == decrypted_content:
        print("Decryption successful: The decrypted text matches the original.")
        return True
    else:
        print("Decryption failed: The decrypted text does not match the original.")
    
        return False

def main():
    # Read shift values
    shift1, shift2 = read_shift_values()
    
    # Read original file
    raw_content = read_file(RAW_FILE_PATH)
    if not raw_content:
        print(f"{RAW_FILE_PATH} is empty or not found. Exiting.")
        return
    
    print(f"Original content length: {len(raw_content)} characters")
    
    # Encrypt
    encrypted_content = encrypt_text(raw_content, shift1, shift2)
    write_file(ENCRYPTED_FILE_PATH, encrypted_content)
    print(f"Encrypted content written to '{ENCRYPTED_FILE_PATH}'")
    
    # Decrypt
    encrypted_content_from_file = read_file(ENCRYPTED_FILE_PATH)
    decrypted_content = decrypt_text(encrypted_content_from_file, shift1, shift2)
    write_file(DECRYPTED_FILE_PATH, decrypted_content)
    print(f"Decrypted content written to '{DECRYPTED_FILE_PATH}'")
    
    # Verify
    verify_decryption(RAW_FILE_PATH, DECRYPTED_FILE_PATH)

if __name__ == "__main__":
    main()