# MyCompanion 🐶

MyCompanion is a desktop pet application that displays a cute dog on your macOS desktop for you to interact with.

## ✨ Key Features (Implemented)
- **Always on Top**: The pet is displayed with a transparent background on top of all other windows.
- **Interactions**: 
  - Hover and move the mouse over the pet to pet it, increasing its happiness.
  - Left or right click the pet to open a context menu (e.g., to feed it).
  - Drag the pet with your mouse to move it around the screen.
- **State Changes**: Over time, the pet gets hungry and changes its state (idle, walking, eating, sleeping, etc.).
- **Data Persistence**: The application remembers the pet's state (hunger, position, etc.) even after it is closed.

## 🛠️ Tech Stack
- **Language**: Python 3
- **GUI Framework**: PyQt6 / PySide6 (Planned)
- **Architecture**: Separation of UI logic and state logic (see `GEMINI.md` for details)

## 📁 Project Structure
- `env/`: Core state transition and interaction logic
- `ui/`: UI-related logic such as rendering, animation, and tray icon
- `assets/`: Resource files including sprite images, GIFs, and icons
- `configs/`: Settings and defaults management
- `utils/`: Common helper functions

## 🚀 Getting Started
Activate the virtual environment and run the main script:

```bash
source .venv/bin/activate
python3 main.py
```

## 📝 Development Log
Detailed development history and daily tasks can be found in the [devlog.md](./devlog.md) file.
