# 🎨 termcolorx

**termcolorx** is a lightweight, dependency-free Python library for stylish terminal output - with full support for **colors**, **text styles**, **emoji icons**, and **ASCII banners/boxes**.  
It’s designed for developers who want readable, expressive CLI applications that *pop with color and energy* 💥

---

## 🚀 Features

- ✅ **ANSI color support** on Windows, macOS, and Linux  
- 💡 Automatically enables **VT Processing** on Windows  
- 🔤 **Text styles**: bold, italic, underline, blink, reverse, dim, hidden  
- 🧱 **ASCII art** helpers (`box` and `banner` styles)  
- 💬 **Semantic printing** helpers: `success()`, `warning()`, `error()`, `info()`  
- 🎭 **Emoji support** in all messages  
- 🧪 **Simple API** - no dependencies, no setup  
- 💻 Works with any standard Python console or terminal emulator

---

## 📦 Installation

You can install it directly from source or package it into a local module:

```bash
pip install termcolorxcore
```

Or if you’re developing locally:
```bash
git clone https://github.com/Luka12-dev/termcolorx.git
cd termcolorx
python setup.py install
```

---

# ⚙️ Basic Usage
```python
from termcolorxcore import colored, success, warning, error, info

print(colored("Hello world!", color="cyan", styles=["bold", "underline"]))
success("Operation completed successfully!")
warning("Low disk space detected.")
error("Failed to connect to server.")
info("System update available.")
```

---

# 🌈 Advanced Examples
- 🧠 Custom color and emoji

```python
from termcolorxcore import custom

custom("User added successfully!", color="bright_green", emoji="🟢")
custom("Custom message", color=95, styles=["bold", "underline"], emoji="✨")
```

# 🧱 ASCII box and banner
```python
from termcolorxcore import success, error

success("Installation Complete", ascii=True)
error("Fatal Error: Missing Dependency", ascii="banner")
```

---

# Output example:

```bash
+------------------------+
| Installation Complete  |
+------------------------+
```

OR

```bash
FATAL ERROR: MISSING DEPENDENCY
================================
```

# 🎯 Input Helpers
- Colored prompts
```python
from termcolorxcore import input_colored, confirm

name = input_colored("Enter your name: ", color="cyan", styles=["bold"])
confirmed = confirm("Are you sure?", default=True)
```

---

# Confirmation dialog
- Returns True for y, yes, 1, true

- Returns False for n, no, 0, false

- Returns the default if input is empty

---

# 🧩 Function Reference
Function	Description
- colored(text, color, styles, emoji)	Returns a styled string
- success(msg, ...)	Prints green success message
- warning(msg, ...)	Prints yellow warning message
- error(msg, ...)	Prints red error message
- info(msg, ...)	Prints blue info message
- custom(msg, color, styles, emoji, ...)	Fully customizable print helper
- input_colored(prompt, color, styles, emoji)	Colored input prompt
- confirm(prompt, default, ...)	Yes/no confirmation input
- asciiize(text, style)	ASCII box/banner rendering
- example_palette()	Returns a string showing all colors
- supports_color()	Checks if the terminal supports ANSI colors

---

# 🎨 Example Palette
```python
from termcolorxcore import example_palette
print(example_palette())
```

Output:

```bash
black  red  green  yellow  blue  magenta  cyan  white  
bright_red  bright_green  bright_yellow  bright_blue  bright_magenta  bright_cyan  bright_white
```

---

# 🧠 Notes
- Colors and styles are combined via ANSI escape sequences.

- On Windows, VT codes are automatically enabled via ctypes.

- If your terminal does not support color, the library falls back gracefully to plain text.

# 📄 License
MIT License © 2025 Luka
Free to use, modify, and distribute with attribution.

# 💪 Motivation
CLI tools don’t have to be boring. With termcolorx, you can make every log, warning, and success message feel alive.
Color isn’t just decoration - it’s clarity, confidence, and communication. 🔥