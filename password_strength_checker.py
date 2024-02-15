import re

def check_password_strength(password):
    # Define criteria for a strong password
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[ !@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password) is None

    # Calculate the score based on criteria
    score = 0
    if not length_error:
        score += 1
    if not digit_error:
        score += 1
    if not uppercase_error:
        score += 1
    if not lowercase_error:
        score += 1
    if not special_char_error:
        score += 1

    # Evaluate the strength based on score
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"

# Main function to take user input and check password strength
def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Your password strength is: {strength}")

if __name__ == "__main__":
    main()
