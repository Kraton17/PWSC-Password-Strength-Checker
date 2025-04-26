# PWSC - Password Strength Checker

PWSC is a Python-based terminal application that evaluates the strength of a given password, checks if it has been involved in any data breaches, estimates its crack time, and suggests a stronger password if necessary.

This tool helps users understand how secure their passwords are and offers suggestions to make them more secure. It checks for common password vulnerabilities such as lack of uppercase, digits, or special characters, and recommends a more robust alternative when needed.

---

## Features

- **Password Strength Evaluation:** Rates the strength of a password on a scale from 0 to 10 based on various criteria.
- **Breach Check:** Checks if the password has been part of any known data breaches using the Have I Been Pwned API.
- **Crack Time Estimate:** Estimates how long it would take for a password to be cracked by brute force.
- **Password Suggestions:** If the password is weak, the tool generates a stronger version with added complexity.

---

## Installation

### Prerequisites

- Python 3.6+ (Make sure you have Python 3 installed)
- `requests` module (for interacting with the Have I Been Pwned API)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/Kraton17/PWSC-Password-Strength-Checker.git
    cd PWSC-Password-Strength-Checker
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

Run the script using:

```bash
python pwsc.py
```

- Enter a password when prompted.
- The tool will display:
  - Password strength
  - Issues found
  - Estimated crack time
  - Whether the password has been found in any data breaches
  - Suggest a stronger password if necessary.

---

## How It Works

- **Password Strength Check:**
  - Evaluates based on length, uppercase, lowercase, digits, special characters.
  - Scores the password from 0 to 10, with explanations for weaknesses.

- **Breach Check:**
  - Checks if the password appeared in any known data breaches (using SHA-1 hash).

- **Crack Time Estimate:**
  - Calculates estimated brute-force crack time based on complexity.

- **Password Suggestions:**
  - Generates a stronger, more complex password if necessary.

---

## Example Output

```
═══════════════════════════════════════════════════
          Password Strength Checker 
═══════════════════════════════════════════════════

Password Strength: 2/10 - Digital Paper Bag 💀
→ A toddler with a dictionary could break this in seconds

Issues found:
- ❌ Too short, rookie. I could brute-force this in my sleep 😴
- ❌ No uppercase? Even script kiddies would laugh at this 🙄
- ❌ No digits? A 5-year-old could guess this 📟
- ❌ No special characters? Add some spice, bro 🔥

⚠ Found in 120226 data breaches! Not safe.
🛡 Estimated Crack Time: Less than a second ⚠ – basically already cracked

✨ Suggested Strong Password: Okn81Hg2

═══════════════════════════════════════════════════

Press any key to exit...
```

---

## Contributing

If you want to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request with your improvements or bug fixes.

---

## Contact

Feel free to reach out with any questions or suggestions!

- GitHub: [Kraton17](https://github.com/Kraton17)
