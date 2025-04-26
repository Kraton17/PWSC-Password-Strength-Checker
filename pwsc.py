import string
import hashlib
import requests
import random
import curses

# Helper function for elite substitutions
def elite_substitute(char):
    elite_dict = {
        'a': '@', 'b': '8', 'e': '3', 'g': '9', 'i': '1',
        'l': '1', 'o': '0', 's': '$', 't': '7', 'z': '2'
    }
    return elite_dict.get(char, char)

# Check password strength
def check_password_strength(password):
    reasons = []
    score = 0

    if len(password) >= 8:
        score += 2
    else:
        reasons.append("Too short, rookie. I could brute-force this in my sleep 😴")

    if any(c.isupper() for c in password):
        score += 2
    else:
        reasons.append("No uppercase? Even script kiddies would laugh at this 🙄")

    if any(c.islower() for c in password):
        score += 2
    else:
        reasons.append("No lowercase? What is this, a CAPTCHA test? 🤨")

    if any(c.isdigit() for c in password):
        score += 2
    else:
        reasons.append("No digits? A 5-year-old could guess this 📟")

    if any(c in string.punctuation for c in password):
        score += 2
    else:
        reasons.append("No special characters? Add some spice, bro 🔥")

    if score >= 9:
        strength = "Vault of the Gods 🔐 – Only AI might stand a chance against this 🔥"
    elif score >= 6:
        strength = "Fortress on Fire 🏰🔥 – Solid, but a determined bot could find a backdoor"
    else:
        strength = "Digital Paper Bag 💀 – A toddler with a dictionary could break this in seconds"

    return strength, reasons, score

# Check if password was breached
def check_breached_password(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            hashes = response.text.splitlines()
            for line in hashes:
                h_suffix, count = line.split(':')
                if h_suffix.lower() == suffix.lower():
                    return int(count)
    except:
        pass
    return 0

# Estimate crack time
def estimate_crack_time(password):
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)

    total = pool ** len(password)
    guesses_per_sec = 1_000_000_000
    seconds = total / guesses_per_sec

    if seconds < 1:
        return "Less than a second ⚠️ – basically already cracked"
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365.25

    if years >= 100:
        return f"{int(years)}+ years – even quantum computers gonna cry 💀"
    elif years >= 1:
        return f"{int(years)} years"
    elif days >= 1:
        return f"{int(days)} days"
    elif hours >= 1:
        return f"{int(hours)} hours"
    elif minutes >= 1:
        return f"{int(minutes)} minutes"
    else:
        return f"{int(seconds)} seconds"

# Mutate password for better security
def mutate_password(password, extra_length=4):
    mutated = []
    for char in password:
        if char.islower():
            mutated.append(random.choice([char.upper(), char, elite_substitute(char)]))
        elif char.isupper():
            mutated.append(random.choice([char.lower(), char, elite_substitute(char.lower())]))
        elif char.isdigit():
            mutated.append(random.choice([char, random.choice('!@#$%^&*')]))
        else:
            mutated.append(random.choice([char, random.choice(string.ascii_letters)]))

    entropy_pool = string.ascii_letters + string.digits + string.punctuation
    for _ in range(extra_length):
        mutated.append(random.choice(entropy_pool))

    random.shuffle(mutated)
    return ''.join(mutated)

# Main UI
def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_CYAN, -1)     # Title color
    curses.init_pair(2, curses.COLOR_GREEN, -1)    # Good message
    curses.init_pair(3, curses.COLOR_RED, -1)      # Warning/bad message
    curses.init_pair(4, curses.COLOR_YELLOW, -1)   # Issues
    curses.init_pair(5, curses.COLOR_MAGENTA, -1)  # Password suggestions

    stdscr.clear()
    curses.curs_set(1)

    # Header
    stdscr.addstr(1, 2, "═══════════════════════════════════════════════════", curses.color_pair(1))
    stdscr.addstr(2, 10, "     Password Strength Checker (PWSC) ", curses.color_pair(1) | curses.A_BOLD)
    stdscr.addstr(3, 2, "═══════════════════════════════════════════════════", curses.color_pair(1))

    # Input
    stdscr.addstr(5, 2, "[+] Enter your password to check:", curses.color_pair(2))
    curses.echo()
    password = stdscr.getstr(7, 2, 40).decode('utf-8')

    stdscr.clear()

    # Re-draw Header
    stdscr.addstr(1, 2, "═══════════════════════════════════════════════════", curses.color_pair(1))
    stdscr.addstr(2, 10, "     Password Strength Checker (PWSC) ", curses.color_pair(1) | curses.A_BOLD)
    stdscr.addstr(3, 2, "═══════════════════════════════════════════════════", curses.color_pair(1))

    strength, issues, score = check_password_strength(password)

    stdscr.addstr(5, 2, f"Password Strength: {score}/10 - {strength.split('–')[0].strip()}", curses.color_pair(2) | curses.A_BOLD)
    stdscr.addstr(6, 4, f"→ {strength.split('–')[1].strip()}", curses.color_pair(5))
    stdscr.addstr(7, 2, "═══════════════════════════════════════════════════", curses.color_pair(1))

    if issues:
        stdscr.addstr(9, 2, "Issues found:", curses.color_pair(3) | curses.A_BOLD)
        for idx, issue in enumerate(issues, start=1):
            stdscr.addstr(10 + idx, 4, f"- ❌ {issue}", curses.color_pair(4))
        line = 11 + len(issues)
    else:
        line = 9

    # Breach Check
    breach_count = check_breached_password(password)
    if breach_count > 0:
        stdscr.addstr(line + 2, 2, f"⚠️ Found in {breach_count} data breaches! Not safe.", curses.color_pair(3) | curses.A_BOLD)
    else:
        stdscr.addstr(line + 2, 2, "✅ Password is safe (not found in breaches).", curses.color_pair(2) | curses.A_BOLD)

    # Crack Time
    crack_time = estimate_crack_time(password)
    stdscr.addstr(line + 4, 2, f"🛡️ Estimated Crack Time: {crack_time}", curses.color_pair(5))
    stdscr.addstr(line + 5, 2, "═══════════════════════════════════════════════════", curses.color_pair(1))

    # Suggest strong password
    if score >= 7:
        stdscr.addstr(line + 7, 2, "[?] Your password is already strong.", curses.color_pair(2))
        stdscr.addstr(line + 8, 2, "    Do you want an even stronger version? (y/n): ", curses.color_pair(2))
        curses.echo()
        choice = stdscr.getstr(line + 9, 2, 3).decode('utf-8').lower()
        if choice == 'y':
            strong_password = mutate_password(password)
            stdscr.addstr(line + 11, 2, f"✨ Suggested Strong Password: {strong_password}", curses.color_pair(5))
    else:
        strong_password = mutate_password(password)
        stdscr.addstr(line + 7, 2, f"✨ Suggested Strong Password: {strong_password}", curses.color_pair(5))

    stdscr.addstr(line + 9 + 5, 2, "═══════════════════════════════════════════════════", curses.color_pair(1))
    stdscr.addstr(line + 11 + 5, 2, "Press any key to exit...", curses.color_pair(2))
    stdscr.getch()

curses.wrapper(main)
