import re

# List of common weak passwords (expand this list as needed)
COMMON_PASSWORDS = {"123456", "password", "qwerty", "abc123", "letmein", "monkey", "football"}

def check_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) < 8:
        feedback.append("Password is too short (must be at least 8 characters).")
    else:
        score += 1  # Length is sufficient

    # Check for uppercase, lowercase, numbers, and special characters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    # Check if password is too common
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This password is too common and easily guessed.")
        score = 1  # Override score if it's a known weak password

    # Determine strength rating
    if score == 5:
        return "Strong Password!", feedback
    elif score >= 3:
        return "Moderate Password", feedback
    else:
        return "Weak Password", feedback

# Run the script
if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    strength, suggestions = check_password_strength(user_password)
    
    print("\nPassword Strength:", strength)
    if suggestions:
        print("Suggestions for improvement:")
        for tip in suggestions:
            print("- " + tip)
