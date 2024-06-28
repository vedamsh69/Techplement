import sys
import random
import os
from datetime import datetime

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_characters = "!@#$%^&*()-_+=<>?/"

    character_pool = ""

    if use_uppercase:
        character_pool += uppercase_letters
    if use_lowercase:
        character_pool += lowercase_letters
    if use_digits:
        character_pool += digits
    if use_special:
        character_pool += special_characters

    if not character_pool:
        print("Error: No character types selected. Please select at least one character type.")
        return ""

    password = "".join(random.choice(character_pool) for _ in range(length))
    return password

def save_password_to_file(password):
    directory = "passwords"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    filename = f"password_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    file_path = os.path.join(directory, filename)

    with open(file_path, "w") as file:
        file.write(f"Generated Password: {password}\n")
    
    print(f"Password saved to: {file_path}")

def main():
    args = sys.argv[1:]
    print(f"Arguments: {args}")  # Add this line to check arguments

    if "--length" not in args:
        print("Error: Length not specified. Use --length <length> to specify the password length.")
        return

    length_index = args.index("--length") + 1

    if length_index >= len(args):
        print("Error: Length value missing.")
        return

    try:
        length = int(args[length_index])
    except ValueError:
        print("Error: Length must be an integer.")
        return

    use_uppercase = "--uppercase" in args
    use_lowercase = "--lowercase" in args
    use_digits = "--digits" in args
    use_special = "--special" in args

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    
    if password:
        print(f"Generated Password: {password}")
        save_password_to_file(password)

if __name__ == "__main__":
    main()