# 🔐 Password Generator

A Python-based GUI password generator built using **Tkinter** in PyCharm. This tool allows users to generate secure passwords based on their selected strength (Weak, Medium, Strong) and desired length. The generated password can be easily copied to the clipboard using the `pyperclip` module.

---

## 📚 Table of Contents

- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Requirements](#-requirements)
- [How It Works](#how-it-works)
- [How to Run](#-how-to-run)
- [Preview](#-preview)
- [License](#-license)

---

## 🚀 Features

- Graphical User Interface (GUI) using Tkinter
- Choose password strength: **Weak**, **Medium**, or **Strong**
- Set custom password length
- Generates a secure, random password
- **One-click copy** to clipboard using `pyperclip`
- Clean and intuitive design

---

## 🧰 Technologies Used

- Python 3.x
- Tkinter – for building the GUI
- pyperclip – for clipboard functionality
- PyCharm – as the development environment

---

## 📌 Requirements

- Python 3.x
- `pyperclip` module

### Install dependencies:

```bash
pip install pyperclip
```

Tkinter comes pre-installed with most Python distributions.

---

## 🛠️ How It Works

1. Launch the GUI window.
2. Select the desired **password strength**:
   - **Weak**: Lowercase letters only
   - **Medium**: Lowercase + Uppercase + Digits
   - **Strong**: Lowercase + Uppercase + Digits + Special Characters
3. Enter the **desired length** of the password.
4. Click the **Generate** button.
5. The password will be displayed in a text box and **copied to your clipboard** automatically.

---

## 💻 How to Run

### Clone the repository:

```bash
git clone https://github.com/sanjana0329/assword-Generator.git
cd password-generator
```

### Run the script:

```bash
python password_generator.py
```

---


## 📷 Preview

> _Below are screenshots of the GUI application in action:_

### 🟢 Main Interface

![Main Interface](screenshot.png)

### 🟡 Example: After Password Generation

![After Generation](screenshot_after.png)




## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
