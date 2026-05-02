# MyCompanion - Project Rules & Architecture

## Purpose
This file defines repository-specific working rules for coding agents on the MyCompanion project.
Prefer these rules over generic habits when they conflict.

## Repository Structure
*   `env/`: Core environment logic, pet state transitions, and interaction handling (State Agent, Interaction Agent).
*   `agents/`: Agent definitions, autonomous behaviors (e.g., wandering, reacting to hunger), and state serialization (Persistence Agent).
*   `configs/`: Shared defaults, application settings, and UI themes.
*   `scripts/`: Runnable CLI entry points for testing, standalone components, or building the app.
*   `utils/`: Shared helpers used by scripts, environment, and UI.
*   `ui/`: PyQt/PySide rendering, animations, system tray integration, and frameless window logic (UI & Rendering Agent).
*   `outputs/`: Generated artifacts (logs, temporary state saves, compiled assets).
*   `assets/`: (New) Sprites, GIFs, icons, and sounds used by the pet.

## Architecture Rules
*   Keep entry points (e.g., `main.py`) thin. Put reusable logic in `utils/`, `agents/`, `env/`, or `ui/`.
*   Keep core state logic (e.g., hunger decay, happiness calculation) completely separate from UI-only rendering code.
*   Preserve state save compatibility (e.g., JSON schema) unless there is a clear migration plan.

## State and Interaction Rules
*   The core state should include (hunger, happiness, current_action, position_x, position_y). Do not change that casually.
*   If interaction mechanics change (e.g., adding "play fetch"), verify that state updates and UI animations interpret the changes correctly.

## Persistence Rules
*   Keep the save file naming predictable (e.g., `pet_state.json`).
*   Prefer extending centralized `save()` and `load()` functions over adding one-off serialization paths.
*   If the save schema changes, document compatibility impact in the change summary.

## UI Rules
*   Keep layout constants (window size, transparency levels) and menu behavior (context menu) centralized in `ui/` or `configs/`.
*   Do not hardcode hyperparameter defaults (e.g., animation speed, update intervals) across multiple UI files.

## Coding Style Rules
*   All code comments must be written in English.

## Documentation Rules
*   Keep a daily record of progress, decisions, and milestones in devlog.md.
*   Update devlog.md at the end of each development session or when a significant feature is completed.

## Generated Files
*   Treat `outputs/` as generated content.
*   Do not commit caches, logs, or user-specific state saves unless explicitly requested.

## Validation
*   Run lightweight validation for changed code paths when practical.
*   In summaries, state what was validated and what was not.

## Commit Convention
*   Use Conventional Commit style messages (feat: ..., refactor: ..., docs: ..., or chore: ...).
*   Keep the subject line lowercase, concise, and focused on the main outcome.
