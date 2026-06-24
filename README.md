
# Petal Lock

A cute password strength checker and generator, built in Python.

## What it does

- **Check a password** — get a strength rating (🌱 weak → 🌟 excellent) with a visual bar and specific feedback on how to improve it.
- **Generate a password** — choose a length and whether to include symbols, and get a strong random password instantly.

## Running it

You'll need Python 3 installed. Then, from the project folder:

```bash
python petal_lock.py
```

or, depending on your system:

```bash
python3 petal_lock.py
```

No extra libraries needed — just plain Python.

## How strength is scored

Petal Lock checks for:
- Length (8+ okay, 12+ better, 16+ best)
- A mix of uppercase, lowercase, numbers, and symbols
- Common weak patterns like "password," "123456," or "qwerty"
- Repeated characters in a row (e.g. "aaa")

## Preview

```
==========================================
       🔐  PETAL LOCK  🔐
==========================================
A cute little password checker & generator.

What would you like to do?
  1) Check a password's strength
  2) Generate a new password
  3) Quit
Your choice (1-3): 1

Enter a password to check: ********

Strength: 🌸 Strong
[🌸🌸🌸🌸🌸🌸🌸·]

Feedback:
  • This password looks solid — nice work!
```

Made with ✿ and a little bit of Python.
