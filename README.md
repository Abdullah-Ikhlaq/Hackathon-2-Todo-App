# Todo CLI App 🚀

A stylish, cyberpunk-themed command-line Todo application with in-memory storage, built with Python and **Rich** for a stunning neon console experience.

---

## Features

* **Add tasks** with title and description.
* **View all tasks** in a beautiful neon table with status indicators ([ ] / [X]).
* **Update task details** by ID (press Enter to keep current value).
* **Delete tasks** by ID with confirmation prompt.
* **Toggle task completion** status.
* **Immersive cyberpunk UI** with glowing cyan/magenta panels, icons (✦, 🚀), and rounded borders.

---

## Tech Stack

* **Python 3.13+**: Latest stable Python for modern features.
* **UV**: Ultra-fast Python project and dependency manager.
* **Rich**: Terminal styling, layouts, and tables for the "cyberpunk" aesthetic.

---

## Project Structure

```text
todo-console-app/
├── .gitignore                        # Files to exclude from Git (like .venv)
├── pyproject.toml                    # UV project configuration
├── uv.lock                           # Locked dependency versions
├── README.md                         # Project documentation
├── src/
│   ├── todo.py                       # Task dataclass + TodoManager logic
│   ├── cli.py                        # Rich-powered cyberpunk UI components
│   └── main.py                       # Application entry point & main loop
└── specs_history/                    # Iterative design specifications
    ├── spec_v1_initial.yaml
    └── ...

```

---

## 🛠️ Setup & Installation

Follow these steps to get the environment ready:

1. **Check Python Version** Ensure you have **Python 3.13+** installed on your system.
2. **Install UV** If you don't have it yet, install the `uv` package manager:
```bash
pip install uv

```


3. **Clone & Navigate** Clone the repository and enter the project directory:
```bash
git clone <your-repo-url>
cd todo-console-app

```

4. **Sync Environment** Create the virtual environment and install dependencies automatically:
```bash
uv sync

```

---

## 🚀 Running the Application

To launch the CLI, simply run:

```bash
uv run src/main.py

```

### Main Menu Guide

* `1` → **Create**: Add a new task with a title and description.
* `2` → **Read**: Display your task list in the neon table.
* `3` → **Update**: Modify an existing task's text.
* `4` → **Delete**: Remove a task permanently.
* `5` → **Complete**: Toggle the `[ ]` to an `[X]`.
* `0` → **Exit**: Close the app with a friendly goodbye.

---

## Usage Examples

### Adding a Task

```text
→ Enter your choice: 1
Enter task title: Finish hackathon project
Enter task description: Implement all Phase I features with style
Task added successfully with ID 1.

```

### Viewing the Dashboard

```text
Your Tasks
┌────┬────────┬──────────────────────────┬────────────────────────────────────┐
│ ID │ Status │ Title                    │ Description                        │
├────┼────────┼──────────────────────────┼────────────────────────────────────┤
│  1 │  [ ]   │ Finish hackathon project │ Implement all Phase I features ... │
└────┴────────┴──────────────────────────┴────────────────────────────────────┘

```

### Marking as Complete

```text
→ Enter your choice: 5
Enter task ID: 1
Task 1 marked as complete! ✦

```

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

```
