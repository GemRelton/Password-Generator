import random
import string

def generate_password(length=12, include_upper=True, include_digits=True, include_special=True):
    """
    Generates a random password.
    
    Args:
        length (int): Length of the password (default is 12).
        include_upper (bool): Include uppercase letters (default is True).
        include_digits (bool): Include digits (default is True).
        include_special (bool): Include special characters (default is True).
    
    Returns:
        str: The generated password.
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_upper else ''
    digits = string.digits if include_digits else ''
    special = string.punctuation if include_special else ''
    
    if not (lower or upper or digits or special):
        raise ValueError("At least one character set must be included.")
    
    all_characters = lower + upper + digits + special
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    # Ensure password includes at least one of each selected character type
    if include_upper:
        password = password[:length] + random.choice(upper)
    if include_digits:
        password = password[:length-1] + random.choice(digits)
    if include_special:
        password = password[:length-1] + random.choice(special)
    
    return ''.join(random.sample(password, len(password)))  # Shuffle to ensure randomness

def save_password(password, filename="passwords.txt"):
    """
    Saves the generated password to a file.
    
    Args:
        password (str): The password to save.
        filename (str): The file to save the password in (default is 'passwords.txt').
    """
    with open(filename, "a") as file:
        file.write(password + "\n")
    print(f"Password saved to {filename}.")

def main():
    print("Password Generator")
    length = int(input("Enter the desired password length (default is 12): ") or 12)
    include_upper = input("Include uppercase letters? (y/n, default is y): ").lower() in ['y', 'yes', '']
    include_digits = input("Include digits? (y/n, default is y): ").lower() in ['y', 'yes', '']
    include_special = input("Include special characters? (y/n, default is y): ").lower() in ['y', 'yes', '']
    
    try:
        password = generate_password(length, include_upper, include_digits, include_special)
        print(f"Generated Password: {password}")
        save = input("Do you want to save this password? (y/n): ").lower() in ['y', 'yes']
        if save:
            save_password(password)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
