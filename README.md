# 🧮 Modern Tkinter Calculator

<img src="https://github.com/manav2001-coder/Tkinter-Calculator/raw/main/calc.png" alt="Screenshot of the Tkinter Calculator" height="700" width="350">

A sleek, lightweight, and fully functional desktop calculator built using Python and the **Tkinter** library. This project focuses on a modern, flat-design UI with a "Midnight Blue" color scheme, making it both visually appealing and easy to use.

---

## ✨ Features

* **Clean, Modern UI:** High-contrast buttons with a flat design for a minimalist look.
* **Fixed Window Size:** The application window is set to a non-resizable `300x400` pixels, ensuring a consistent user experience across different systems.
* **Intuitive Color-Coding:**
    * 🟢 **Green:** Calculate Result (`=`)
    * 🔴 **Red:** Clear Display (`C`)
    * 🟠 **Orange:** Arithmetic Operators (`+`, `-`, `*`, `/`)
* **Robust Error Handling:** Displays a clear "Error" message for invalid mathematical expressions (e.g., division by zero).

## 🛠️ Installation & Usage

### Prerequisites

Ensure you have **Python 3.x** installed on your system. Tkinter is typically included by default with Python installations.

### Running the Calculator

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/manav2001-coder/Tkinter-Calculator.git](https://github.com/manav2001-coder/Tkinter-Calculator.git)
    cd Tkinter-Calculator
    ```
2.  **Execute the Script:**
    ```bash
    python calculator_app.py # (Assuming your main file is named calculator_app.py)
    ```

## ⌨️ How to Use

Simply click the number and operator buttons to build your mathematical expression.
* Press `=` to see the result.
* Press `C` to clear the display.

## 🎨 Design & Styling

The calculator adopts a specific color palette to enhance its modern aesthetic:

| Element            | Hex Code | Description          |
| :----------------- | :------- | :------------------- |
| **Background** | `#2c3e50` | Midnight Blue        |
| **Display Text** | `#ecf0f1` | Light Grey (off-white) |
| **Clear Button** | `#e74c3c` | Alizarin Red         |
| **Equal Button** | `#2ecc71` | Emerald Green        |
| **Operator Buttons** | `#e67e22` | Carrot Orange        |
| **Number Buttons** | `#34495e` | Darker Blue-Grey     |

## ⚠️ macOS Users: Color Display Issues

If you're running this on macOS and the button colors (`bg`) are not appearing as intended, this is a common Tkinter limitation on Mac due to its native "Aqua" theme.

To fix this, you can install and use the `tkmacosx` library:

1.  **Install `tkmacosx`:**
    ```bash
    pip install tkmacosx
    ```
2.  **Update your Python script:**
    * Change `import tkinter as tk` to `import tkinter as tk` and `from tkmacosx import Button`.
    * Replace `tk.Button` with `Button` when creating your buttons.

---

*Made by [Manav](https://github.com/manav2001-coder)*