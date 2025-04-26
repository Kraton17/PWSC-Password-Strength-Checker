PWSC - Password Strength Checker

**PWSC** is a Python-based terminal application that evaluates the strength of a given password, checks if it has been involved in any data breaches, estimates its crack time, and suggests a stronger password if necessary.

This tool is built to help users understand how secure their passwords are and offers suggestions to make them more secure. It checks for common password vulnerabilities, such as lack of uppercase, digits, or special characters, and recommends a more robust alternative when needed.

---

## Features

- **Password Strength Evaluation**: Rates the strength of a password on a scale from 0 to 10 based on various criteria.
- **Breach Check**: Checks if the password has been part of any known data breaches using the Have I Been Pwned API.
- **Crack Time Estimate**: Estimates how long it would take for a password to be cracked by brute force.
- **Password Suggestions**: If the password is weak, the tool generates a stronger version with added complexity.

---

## Installation

### Prerequisites

Before running the project, you need to install the following dependencies:

1. Python 3.6+ (Make sure you have Python 3 installed on your machine).
2. Requests module to interact with the `Have I Been Pwned` API.

You can install the dependencies using the following command:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

---

## Usage

### Running the Tool

1. Clone the repository to your local machine:

    \`\`\`bash
    git clone https://github.com/your-username/PWSC-Password-Strength-Checker.git
    cd PWSC-Password-Strength-Checker
    \`\`\`

2. Run the script with the following command:

    \`\`\`bash
    python pwsc.py
    \`\`\`

3. Enter a password when prompted, and the tool will display its strength, any issues, estimated crack time, and if it's been breached. If necessary, it will also suggest a stronger password.

---

## How It Works

1. **Password Strength Check**: 
    - The strength is calculated based on several factors like length, use of uppercase, lowercase, digits, and special characters.
    - The strength is rated on a scale from 0 to 10, with explanations for the weaknesses.

2. **Breach Check**:
    - The tool checks if the password has appeared in any data breaches using the Have I Been Pwned API (using the SHA-1 hash of the password).

3. **Crack Time Estimate**:
    - Based on the complexity of the password, the tool estimates how long it would take to crack the password using brute force.

4. **Password Suggestions**:
    - If the password is weak, the tool generates a stronger, more complex version of the password.

---

## Example Output

\`\`\`
═══════════════════════════════════════════════════
     Password Strength Checker (PWSC) 
═══════════════════════════════════════════════════
[+] Enter your password to check:

Nishad

Password Strength: 4/10 - Digital Paper Bag 💀 – A toddler with a dictionary could break this in seconds

Issues found:
- ❌ Too short, rookie. I could brute-force this in my sleep 😴
- ❌ No digits? A 5-year-old could guess this 📟
- ❌ Add some spice, bro. Special chars are the 🔑 to chaos.

⚠️ Found in 333 data breaches! Not safe.
🛡️ Estimated Crack Time: 19 seconds

✨ Suggested Strong Password: MhIdnW'SDA

═══════════════════════════════════════════════════
Press any key to exit...
\`\`\`

---

## Contributing

If you want to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request with your improvements or bug fixes.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

Feel free to reach out with any questions or suggestions. You can contact me at:

- Email: [your-email@example.com](mailto:your-email@example.com)
- GitHub: [your-username](https://github.com/your-username)
