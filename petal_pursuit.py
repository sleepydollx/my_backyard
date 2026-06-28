"""
Petal Pursuit — a cozy number-guessing game with a hot/cold twist.

How to play:
- The game picks a secret number in a range you choose.
- You guess numbers, and instead of plain "higher/lower," you get
  a warmth rating telling you how close you are.
- Try to find it in as few guesses as possible for a better rank!

Run it with: python petal_pursuit.py
"""

import random

DIFFICULTIES = {
    "1": ("cozy",    1, 50,  10),
    "2": ("breezy",  1, 100, 8),
    "3": ("stormy",  1, 500, 12),
}

RANK_TITLES = [
    (1, "🌟 Petal Whisperer — perfect guess!"),
    (3, "🌸 Bloom Master"),
    (5, "🌷 Garden Friend"),
    (8, "🍃 Wandering Sprout"),
    (999, "🌱 Patient Seedling"),
]


def choose_difficulty():
    print("\nChoose your garden:")
    print("  1) cozy    (1-50,  10 guesses)")
    print("  2) breezy  (1-100, 8 guesses)")
    print("  3) stormy  (1-500, 12 guesses)")

    choice = input("Your choice (1-3): ").strip()
    return DIFFICULTIES.get(choice, DIFFICULTIES["1"])


def warmth_message(guess, secret, lo, hi):
    distance = abs(guess - secret)
    span = hi - lo
    ratio = distance / span if span else 0

    if distance == 0:
        return "🔥🔥🔥 You found it!!"
    elif ratio < 0.03:
        return "🔥 Blazing hot — so close!"
    elif ratio < 0.08:
        return "🌡️ Very warm"
    elif ratio < 0.15:
        return "☁️ Warm"
    elif ratio < 0.3:
        return "🍃 Cool"
    else:
        return "❄️ Freezing cold"


def direction_hint(guess, secret):
    if guess < secret:
        return "Try going higher."
    elif guess > secret:
        return "Try going lower."
    return ""


def rank_for_attempts(attempts):
    for threshold, title in RANK_TITLES:
        if attempts <= threshold:
            return title
    return RANK_TITLES[-1][1]


def play_round():
    name, lo, hi, max_guesses = choose_difficulty()
    secret = random.randint(lo, hi)

    print(f"\nYou're in the {name} garden! Find the hidden number between {lo} and {hi}.")
    print(f"You have {max_guesses} guesses. Good luck! 🌷\n")

    for attempt in range(1, max_guesses + 1):
        guess_input = input(f"Guess #{attempt}: ").strip()

        if not guess_input.isdigit():
            print("Please enter a whole number.\n")
            continue

        guess = int(guess_input)

        if guess < lo or guess > hi:
            print(f"Stay within {lo}-{hi}, please!\n")
            continue

        if guess == secret:
            print(f"\n{warmth_message(guess, secret, lo, hi)}")
            print(f"You got it in {attempt} guess(es)!")
            print(rank_for_attempts(attempt))
            return True

        print(warmth_message(guess, secret, lo, hi))
        print(direction_hint(guess, secret))
        print()

    print(f"\nOut of guesses! The number was {secret}. The garden grows quiet... 🌙\n")
    return False


def main():
    print("=" * 42)
    print("       🌷  PETAL PURSUIT  🌷")
    print("=" * 42)
    print("Find the hidden number using warmth clues!")

    wins = 0
    rounds = 0

    while True:
        rounds += 1
        if play_round():
            wins += 1

        print(f"\nScore so far: {wins} win(s) out of {rounds} round(s)")
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\nThanks for visiting Petal Pursuit! ✿ See you again soon.")


if __name__ == "__main__":
    main()