
def check_password_strength(password):
    # Criteria flags (True/False)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_=+[]{};:'\",.<>/?`~" for char in password)
    is_long = len(password) >= 12

    # Calculate score
    score = 0
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    if is_long:
        score += 1

    # Determine strength
    if score == 5:
        return "Very Strong!"
    elif score >= 3:
        return "Strong!"
    elif score >= 2:
        return "Moderate!"
    else:
        return "Weak!"

# Main program
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")