# MyCompanion Development Log

This file tracks the daily progress, decisions, and milestones of the MyCompanion project.

## 2026-05-01
- **Project Initialized**: Set up the project structure (`env/`, `ui/`, `assets/`, `configs/`, `scripts/`, `utils/`) and defined architecture rules in `GEMINI.md`.
- **Environment Setup**: Created Python virtual environment and installed required packages (`PySide6`, `Pillow`, `pystray`).
- **Core UI Foundation**: Implemented a transparent, frameless window using PySide6 (`ui/pet_window.py`). The window correctly stays on top of other applications.
- **Asset Integration**: Received and processed high-quality, transparent animated GIFs for the pet (`idle.gif`, `petting.gif`, `eating.gif`).
- **Interactions implemented**:
  - **Drag and Drop**: The pet can be moved around the screen.
  - **Petting**: Hovering and moving the mouse over the pet triggers the petting animation (`petting.gif`) for 3 seconds.
  - **Feeding & Context Menu**: Left or right clicking opens a context menu with 'Feed' (triggers `eating.gif` for 4 seconds) and 'Quit' options.
- **Visual Adjustments**: Reduced the rendering size of the pet by 50% using `QMovie.setScaledSize` without altering the original assets. Set the default spawn location to the bottom-right corner of the primary screen.

## 2026-05-02
- **UI Interaction Update**: Modified `ui/pet_window.py` to trigger the petting interaction on mouse hover and movement, rather than clicking. Dropdown context menu is now triggered on both left and right clicks.
- **Documentation Translation**: Translated all project documentation (`README.md`, etc.) to English to maintain consistency.
