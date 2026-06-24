"""
Petal Lock — a cute password strength checker and generator.

Features:
- Check how strong an existing password is, with feedback on how to improve it.
- Generate a new strong password to a length you choose.

Run it with: python petal_lock.py
"""

import random
import re
import string

RANK_LABELS = [
    (0, "🌱 Very weak"),
    (2, "🍃 Weak"),
    (4, "🌷 Okay"),
    (6, "🌸 Strong"),
    (8, "🌟 Excellent"),
]

COMMON_PATTERNS = [
    "password", "123456", "qwerty", "letmein", "111111",
    "abc123", "iloveyou", "admin", "welcome",
]


def label_for_score(score):
    label = RANK_LABELS[0][1]
    for threshold, text in RANK_LABELS:
        if score >= threshold:
            label = text
    return label


def check_password(pwd):
    score = 0
    feedback = []

    length = len(pwd)
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Try making it at least 8 characters long, ideally 12+.")

    has_lower = re.search(r"[a-z]", pwd) is not None
    has_upper = re.search(r"[A-Z]", pwd) is not None
    has_digit = re.search(r"\d", pwd) is not None
    has_symbol = re.search(r"[^a-zA-Z0-9]", pwd) is not None

    variety = sum([has_lower, has_upper, has_digit, has_symbol])
    score += variety

    if not has_upper:
        feedback.append("Add at least one uppercase letter.")
    if not has_lower:
        feedback.append("Add at least one lowercase letter.")
    if not has_digit:
        feedback.append("Add at least one number.")
    if not has_symbol:
        feedback.append("Add a symbol like ! @ # or %.")

    lowered = pwd.lower()
    for pattern in COMMON_PATTERNS:
        if pattern in lowered:
            score -= 2
            feedback.append(f"Avoid common words/patterns like '{pattern}'.")
            break

    if re.search(r"(.)\1\1", pwd):
        score -= 1
        feedback.append("Avoid repeating the same character three+ times in a row.")

    score = max(0, score)

    if not feedback:
        feedback.append("This password looks solid — nice work!")

    return score, feedback


def generate_password(length=16, use_symbols=True):
    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+?"

    pools = [letters_lower, letters_upper, digits]
    if use_symbols:
        pools.append(symbols)

    password_chars = [random.choice(pool) for pool in pools]

    all_chars = "".join(pools)
    while len(password_chars) < length:
        password_chars.append(random.choice(all_chars))

    random.shuffle(password_chars)
    return "".join(password_chars[:length])


def print_strength_bar(score, max_score=8):
    filled = min(score, max_score)
    bar = "🌸" * filled + "·" * (max_score - filled)
    print(f"[{bar}]")


def run_checker():
    pwd = input("\nEnter a password to check: ")
    if not pwd:
        print("You didn't enter anything.\n")
        return

    score, feedback = check_password(pwd)
    print(f"\nStrength: {label_for_score(score)}")
    print_strength_bar(score)
    print("\nFeedback:")
    for tip in feedback:
        print(f"  • {tip}")
    print()


def run_generator():
    length_input = input("\nHow long should the password be? (default 16): ").strip()
    length = int(length_input) if length_input.isdigit() else 16
    length = max(6, min(length, 64))

    symbols_input = input("Include symbols? (y/n, default y): ").strip().lower()
    use_symbols = symbols_input != "n"

    new_pwd = generate_password(length, use_symbols)
    score, _ = check_password(new_pwd)

    print(f"\nYour new password: {new_pwd}")
    print(f"Strength: {label_for_score(score)}")
    print_strength_bar(score)
    print()


def main():
    print("=" * 42)
    print("       🔐  PETAL LOCK  🔐")
    print("=" * 42)
    print("A cute little password checker & generator.")

    while True:
        print("\nWhat would you like to do?")
        print("  1) Check a password's strength")
        print("  2) Generate a new password")
        print("  3) Quit")

        choice = input("Your choice (1-3): ").strip()

        if choice == "1":
            run_checker()
        elif choice == "2":
            run_generator()
        elif choice == "3":
            break
        else:
            print("Please choose 1, 2, or 3.")

    print("Stay safe out there! ✿")


if __name__ == "__main__":
    main()