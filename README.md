# 🖥️ MacroPad Configurator — Python + Tkinter

<p align="center">
  <b>A desktop GUI app to configure your RP2040 MacroPad without editing JSON by hand</b>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" alt="Python"></a>
  <a href="https://docs.python.org/3/library/tkinter.html"><img src="https://img.shields.io/badge/GUI-Tkinter-orange" alt="Tkinter"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow" alt="License"></a>
</p>

> **Companion Firmware →** [MacroPad RP2040 Firmware](https://github.com/harsh-gupta-10/macropad-rp2040)

---

## ✨ Features

- 🎨 **Dark-themed UI** — sleek, modern interface built with Tkinter
- 📋 **6 Profiles × 9 Keys** — visually browse and edit every key on your macro pad
- ⌨️ **Basic Config** — one-click key assignment from categorized dropdowns (A–Z, F1–F24, media, etc.)
- 🔧 **Advanced Config** — 2-key or 3-key combos with modifier selection (Ctrl, Alt, Shift, Win)
- 🚀 **Software Launcher** — assign keys to open any app (notepad, chrome, discord, custom path…)
- 📝 **Text/Paragraph Mode** — type full text snippets, line-by-line or as paragraphs
  - ✅ **Shift+Enter support** — optional checkbox so newlines don't send messages in WhatsApp
  - ✅ **Press Enter after typing** — optional auto-submit when text is done
- 🎛️ **Special Keys** — configure encoder rotations, clicks, holds, and mic toggle
- ⚡ **Encoder Speed** — adjust volume and display encoder sensitivity (1–5)
- 💾 **Live JSON sync** — reads/writes directly to `keysfile.json` and `special-keyout.json` on the `O:` drive (CIRCUITPY)

---

## 📸 UI Overview

The app has **6 tabs** in the Key Changer Panel:

| Tab | Purpose |
|---|---|
| **Basic Config** | Assign a single key from categorized dropdown |
| **Advanced** | Build 2-key or 3-key combos with modifiers |
| **Software** | Assign a key to launch an application |
| **Text/Para** | Type text macros with single / line-by-line / paragraph modes |
| **Special Keys** | Configure encoder & mic button actions |
| **Settings** | Adjust encoder speeds |

---

## 📁 Project Structure

```text
├── main.py                        # Application entry point
├── engine.py                      # JSON I/O engine (profiles, settings, special keys)
├── components/
│   ├── config_panel.py            # Key Changer Panel (all 6 tabs)
│   ├── keypad_section.py          # 3×3 visual keypad grid
│   ├── profiles_section.py        # Profile selector buttons
│   └── status_bar.py              # Bottom status bar
├── utils/
│   └── key_config.py              # Key configuration utilities
├── logo.png                       # Application icon
├── special-keyout.json            # Default special key mappings
├── keysfile.json                  # Default key mappings
└── requirements.txt               # Python dependencies

```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+** (Tkinter is bundled with standard Python on Windows)
- Your RP2040 MacroPad connected as drive `O:\` (CIRCUITPY)

### Installation & Run

```bash
# Clone the repository
git clone https://github.com/harsh-gupta-10/macropad-software-python-tkinter.git
cd macropad-software-python-tkinter

# (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate

# Run the app
python main.py
```

> No external dependencies required — the app uses only Python's built-in `tkinter` library.

### Building an Executable

```bash
pip install pyinstaller
pyinstaller main.spec
```

The compiled `.exe` will be in the `dist/` folder.

---

## 📖 How to Use

1. **Connect your MacroPad** — ensure the `O:` drive is accessible
2. **Launch the app** — `python main.py`
3. **Select a profile** — click one of the 6 profile buttons at the top
4. **Select a key** — click any of the 9 keys on the visual keypad
5. **Configure the key** in any tab:
   - **Basic** → pick a category + key → Save
   - **Advanced** → choose modifiers + key → Save
   - **Software** → pick or type an app name → Save
   - **Text/Para** → enter text, choose typing style, toggle Shift+Enter if needed → Save
6. **Changes take effect immediately** — the MacroPad auto-reloads when `keysfile.json` is updated

### Configuring Special Keys

1. Go to the **Special Keys** tab
2. Select the action to configure (e.g. "Volume Encoder - Click")
3. Click **Load Action** to see the current mapping
4. Choose **Keyboard Combo** or **Internal Action** mode
5. Set the keys or action → **Save**

---

## ⚙️ Configuration Files

The app reads and writes two JSON files on the `O:` drive:

| File | Purpose |
|---|---|
| `O:\keysfile.json` | Profile key mappings + settings (encoder speeds, active profiles) |
| `O:\special-keyout.json` | Encoder and mic button special actions |

If the `O:` drive isn't available, the app falls back to local copies in the project directory.

### Key Action Schema

```json
{
  "name": "My Macro",
  "key": ["ctrl", "shift", "s"],
  "action": "key_combo"
}
```

```json
{
  "name": "Open Chrome",
  "key": ["windows"],
  "action": "software",
  "software": "chrome"
}
```

```json
{
  "name": "WhatsApp Message",
  "key": ["text_input"],
  "action": "text_input",
  "text_content": "Hello!\nHow are you?",
  "text_type": "paragraph",
  "text_press_enter": true,
  "text_shift_enter": true
}
```

---

## 🐛 Troubleshooting

| Problem | Fix |
|---|---|
| **"O: drive not accessible"** | Make sure the MacroPad is connected via USB and shows as drive `O:` |
| **Changes not reflecting** | Verify save was successful (check the success popup). Open `O:\keysfile.json` to confirm. |
| **App won't start** | Ensure Python 3.10+ is installed with Tkinter (`python -c "import tkinter"`) |
| **Key not configured** | Select both a **profile** and a **key** on the visual keypad before saving |

---

## 📄 License

MIT © [Harsh Gupta](https://github.com/harsh-gupta-10)
