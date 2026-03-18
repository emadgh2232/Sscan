# Sscan - Advanced OSINT Username Checker 🔍🛡️

**Sscan** is a lightweight and efficient Open Source Intelligence (OSINT) tool built in Python. It is designed to perform reconnaissance on specific usernames across multiple social media platforms with high accuracy, detecting both public and private profiles.

## ✨ Features
- **Heuristic Detection**: Unlike basic checkers that rely only on HTTP 200 codes, Sscan analyzes page content to verify if a profile truly exists.
- **Privacy Awareness**: Specifically identifies **Steam** profiles even when set to private, ensuring no lead is missed.
- **Automated Reporting**: Automatically generates a structured `.txt` report for every scan, making documentation easy for investigators.
- **Professional CLI**: Features a clean ASCII banner and organized terminal output for a smooth user experience.

## 🛠️ Supported Platforms
The tool currently supports accurate scanning for:
- **GitHub** 
- **Telegram** 
- **Chess.com** 
- **Steam**
- **YouTube** 

## 🚀 Installation & Usage
1. Ensure you have **Python 3.x** installed.
2. Download `Sscan.py`.
3. Install the required dependency:
   ```bash
   pip install requests
