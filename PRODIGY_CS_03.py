import re

def check_password_strength(password):
    # Minimum length requirement
    min_length = 8

    # Check length
    if len(password) < min_length:
        return "Weak: Password should be at least {} characters long.".format(min_length)

    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."

    # Check for lowercase letters
    if not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."

    # Check for numbers
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one number."

    # Check for special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password should contain at least one special character."

    return "Strong: Password meets all criteria."

def main():
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()
