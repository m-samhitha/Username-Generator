# utils.py
import random
import string

def load_wordlist():
    # You can add words you want to avoid in usernames
    return {"test", "admin", "user"}

def random_suffix(include_numbers, include_specials):
    suffix = ""
    if include_numbers:
        suffix += random.choice(string.digits)
    if include_specials:
        suffix += random.choice("_-.")
    return suffix

def style_username(base, style):
    if style == "funny":
        return base + random.choice(["Lol", "Haha", "Lmao"])
    elif style == "aesthetic":
        return base.lower() + random.choice(["_art", "_vibes", "_x"])
    elif style == "edgy":
        return base.capitalize() + random.choice(["Xx", "_kill", "_dark"])
    else:
        return base

def generate_username(first_name, interests, style, max_length,
                      include_numbers, include_specials, blacklist):
    tries = 0
    while tries < 20:
        interest = random.choice(interests).strip().lower()
        base = first_name.capitalize() + interest.capitalize()
        username = style_username(base, style)
        username += random_suffix(include_numbers, include_specials)

        # Remove spaces and keep under max_length
        username = username.replace(" ", "")
        if len(username) > max_length:
            username = username[:max_length]

        if username.lower() not in blacklist:
            return username
        tries += 1
    return "User" + random_suffix(include_numbers, include_specials)
