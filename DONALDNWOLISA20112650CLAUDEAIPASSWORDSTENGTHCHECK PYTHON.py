# Donald Nwolisa
# 05/12/2024
# PROGRAMME FOR PASSWORD STRENGTH CHECK

import re

# List of common weak passwords (This can be extended)
common_passwords = ["123456", "password", "123456789", "12345", "qwerty", "abc123"]

def check_password_strength(password):
    # Check if password is empty
    if not password:
        return "Very Weak: Password cannot be empty."
    
    # Check for minimum length (8 characters)
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    
    # Check for common passwords
    if password.lower() in common_passwords:
        return "Very Weak: This password is too common."
    
    # Check for criteria: uppercase, lowercase, digits, special characters
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'[0-9]', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    missing_criteria = []
    
    # Collect missing criteria
    if not has_upper:
        missing_criteria.append("uppercase letter")
    if not has_lower:
        missing_criteria.append("lowercase letter")
    if not has_digit:
        missing_criteria.append("digit")
    if not has_special:
        missing_criteria.append("special character")
    
    # Provide detailed feedback
    if missing_criteria:
        return f"Weak: Your password is missing the following criteria: {', '.join(missing_criteria)}."

    # Calculate password strength score based on criteria
    strength_score = 0
    
    # Add score for each criterion
    if has_upper:
        strength_score += 20
    if has_lower:
        strength_score += 20
    if has_digit:
        strength_score += 20
    if has_special:
        strength_score += 20
    
    # Add score for length (length > 12 gives an extra 20 points)
    if len(password) > 12:
        strength_score += 20
    elif len(password) >= 10:
        strength_score += 10
    
    # Check final strength score and return appropriate message
    if strength_score >= 80:
        return f"Strong: Your password strength score is {strength_score}/100."
    elif strength_score >= 50:
        return f"Moderate: Your password strength score is {strength_score}/100."
    else:
        return f"Weak: Your password strength score is {strength_score}/100."

# Function to input password and check its strength
def password_strength_checker():
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)
