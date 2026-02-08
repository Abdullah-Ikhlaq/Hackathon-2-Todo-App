# from typing import Optional
# from todo import Task


# def get_task_input() -> tuple[str, str]:
#     """Get title and description input from user"""
#     title = input("Enter task title: ").strip()
#     description = input("Enter task description: ").strip()
#     return title, description


# def get_task_id() -> Optional[int]:
#     """Get task ID input from user with validation"""
#     try:
#         task_id_input = input("Enter task ID: ").strip()
#         if task_id_input.isdigit():
#             return int(task_id_input)
#         else:
#             print("Invalid ID. Please enter a number.")
#             return None
#     except ValueError:
#         print("Invalid ID. Please enter a number.")
#         return None


# def confirm_action(action: str) -> bool:
#     """Get confirmation from user before performing an action"""
#     confirmation = input(f"Are you sure you want to {action}? (y/n): ").strip().lower()
#     return confirmation in ['y', 'yes']


# def display_tasks(tasks):
#     """Display all tasks with proper formatting"""
#     if not tasks:
#         print("No tasks found.")
#         return
    
#     for task in tasks:
#         status = "[X]" if task.completed else "[ ]"
#         print(f"[{task.id}] {status} {task.title}: {task.description}")


# def display_task(task: Task):
#     """Display a single task with proper formatting"""
#     status = "[X]" if task.completed else "[ ]"
#     print(f"[{task.id}] {status} {task.title}: {task.description}")


# def add_task_cli(todo_manager):
#     """Handle the add task CLI flow"""
#     try:
#         title, description = get_task_input()

#         # Validate title
#         if not title or not title.strip():
#             print("Error: Title cannot be empty or whitespace.")
#             return False

#         task_id = todo_manager.add_task(title, description)
#         print(f"Task added successfully with ID {task_id}.")
#         return True
#     except ValueError as e:
#         print(f"Error: {e}")
#         return False
#     except Exception as e:
#         print(f"An unexpected error occurred while adding task: {e}")
#         return False


# def view_tasks_cli(todo_manager):
#     """Handle the view tasks CLI flow"""
#     try:
#         tasks = todo_manager.get_all_tasks()

#         if not tasks:
#             print("No tasks found.")
#             return

#         display_tasks(tasks)
#     except Exception as e:
#         print(f"An error occurred while viewing tasks: {e}")


# def mark_task_complete_cli(todo_manager):
#     """Handle the mark task complete CLI flow"""
#     try:
#         task_id = get_task_id()
#         if task_id is None:
#             return False

#         success = todo_manager.mark_task_complete(task_id)
#         if success:
#             print(f"Task {task_id} marked as {'complete' if todo_manager.get_task_by_id(task_id).completed else 'incomplete'}.")
#             return True
#         else:
#             print(f"Task with ID {task_id} not found.")
#             return False
#     except Exception as e:
#         print(f"An error occurred while marking task complete: {e}")
#         return False


# def update_task_cli(todo_manager):
#     """Handle the update task CLI flow with Enter-to-skip functionality"""
#     try:
#         task_id = get_task_id()
#         if task_id is None:
#             return False

#         # Check if task exists
#         task = todo_manager.get_task_by_id(task_id)
#         if not task:
#             print(f"Task with ID {task_id} not found.")
#             return False

#         # Get new title, allowing Enter to skip
#         new_title_input = input(f"Enter new title (current: '{task.title}', press Enter to skip): ").strip()
#         new_title = new_title_input if new_title_input else task.title

#         # Get new description, allowing Enter to skip
#         new_description_input = input(f"Enter new description (current: '{task.description}', press Enter to skip): ").strip()
#         new_description = new_description_input if new_description_input else task.description

#         success = todo_manager.update_task(task_id, new_title, new_description)
#         if success:
#             print(f"Task {task_id} updated successfully.")
#             return True
#         else:
#             print(f"Failed to update task {task_id}.")
#             return False
#     except Exception as e:
#         print(f"An error occurred while updating task: {e}")
#         return False


# def delete_task_cli(todo_manager):
#     """Handle the delete task CLI flow with confirmation"""
#     try:
#         task_id = get_task_id()
#         if task_id is None:
#             return False

#         # Check if task exists
#         task = todo_manager.get_task_by_id(task_id)
#         if not task:
#             print(f"Task with ID {task_id} not found.")
#             return False

#         # Confirm deletion
#         if not confirm_action(f"delete task {task_id}"):
#             print("Deletion cancelled.")
#             return False

#         success = todo_manager.delete_task(task_id)
#         if success:
#             print(f"Task {task_id} deleted successfully.")
#             return True
#         else:
#             print(f"Failed to delete task {task_id}.")
#             return False
#     except Exception as e:
#         print(f"An error occurred while deleting task: {e}")
#         return False



from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich import box
from todo import Task, TodoManager  # Assuming TodoManager is in todo.py

console = Console()

# Cyberpunk neon colors
TITLE_STYLE = "bold cyan"
ACCENT_STYLE = "bright_magenta"
SUCCESS_STYLE = "bold green"
ERROR_STYLE = "bold red"
WARNING_STYLE = "bold yellow"
BORDER_STYLE = "bright_cyan"

def print_header():
    """Display cyberpunk header with title and welcome."""
    title = "[bold cyan]TODO APP[/]"
    subtitle = "[bright_magenta]✦  Your Ultimate Task Manager ✦[/]"
    
    console.print(title, justify="center", style=TITLE_STYLE)
    console.print(subtitle, justify="center")
    
    welcome_panel = Panel(
        "[white]Welcome! Manage your tasks efficiently with style![/]",
        border_style=BORDER_STYLE,
        padding=(1, 2),
        box=box.ROUNDED,
        expand=False
    )
    console.print(welcome_panel, justify="center")
    console.print("\n")

def print_menu():
    """Display main menu in a neon-bordered panel."""
    menu_text = (
        "[bold cyan]1.[/] Add new todo item\n"
        "[bold cyan]2.[/] View all your todos\n"
        "[bold cyan]3.[/] Update an existing todo\n"
        "[bold cyan]4.[/] Delete a todo\n"
        "[bold cyan]5.[/] Mark a todo as complete/incomplete\n"
        "[bold red]0.[/] Exit the application"
    )
    
    menu_panel = Panel(
        menu_text,
        title="[bold bright_cyan]MAIN MENU[/]",
        border_style=BORDER_STYLE,
        padding=(1, 4),
        box=box.ROUNDED
    )
    console.print(menu_panel)
    console.print("\n[bold yellow]→ Enter your choice:[/] ", end="")

def get_task_input() -> tuple[str, str]:
    """Get title and description with neon prompts."""
    title = Prompt.ask("[bold cyan]Enter task title[/]", default="")
    description = Prompt.ask("[bold cyan]Enter task description[/]", default="")
    return title.strip(), description.strip()

def get_task_id() -> Optional[int]:
    """Get task ID with validation."""
    return IntPrompt.ask("[bold cyan]Enter task ID[/]", default=None)

def confirm_action(action: str) -> bool:
    """Get confirmation with styled prompt."""
    return Prompt.ask(
        f"[bold yellow]Are you sure you want to {action}?[/] (y/n)",
        choices=["y", "n"],
        default="n"
    ) == "y"

def display_tasks(tasks: list[Task]):
    """Display tasks in a neon-styled table."""
    if not tasks:
        console.print(Panel("[italic yellow]No tasks yet. Add one to get started![/]", border_style=WARNING_STYLE))
        return
    
    table = Table(title="[bold cyan]Your Tasks[/]", box=box.ROUNDED, border_style=BORDER_STYLE)
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Status", justify="center")
    table.add_column("Title", style="bold white")
    table.add_column("Description", style="dim white")
    
    for task in tasks:
        status = "[✔]" if task.completed else "[ ]"
        status_color = SUCCESS_STYLE if task.completed else "dim"
        table.add_row(
            str(task.id),
            f"[{status_color}]{status}[/{status_color}]",
            task.title,
            task.description or "[dim]No description[/]"
        )
    
    console.print(table)

def add_task_cli(manager: TodoManager) -> bool:
    """Handle add task with Rich prompts."""
    title, description = get_task_input()
    if not title:
        console.print("[bold red]Error: Title cannot be empty.[/]")
        return False
    
    try:
        task_id = manager.add_task(title, description)
        console.print(Panel(f"[green]Task added successfully with ID {task_id}.[/]", border_style=SUCCESS_STYLE))
        return True
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/]")
        return False

def view_tasks_cli(manager: TodoManager):
    """Handle view tasks with Rich table."""
    try:
        tasks = manager.get_all_tasks()
        display_tasks(tasks)
    except Exception as e:
        console.print(f"[bold red]Error viewing tasks: {e}[/]")

def mark_task_complete_cli(manager: TodoManager) -> bool:
    """Handle mark complete with Rich feedback."""
    task_id = get_task_id()
    if task_id is None:
        return False
    
    try:
        success = manager.mark_task_complete(task_id)
        if success:
            status = "complete" if manager.get_task_by_id(task_id).completed else "incomplete"
            console.print(Panel(f"[green]Task {task_id} marked as {status}.[/]", border_style=SUCCESS_STYLE))
            return True
        else:
            console.print(f"[bold red]Task {task_id} not found.[/]")
            return False
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/]")
        return False

def update_task_cli(manager: TodoManager) -> bool:
    """Handle update with Enter-to-skip."""
    task_id = get_task_id()
    if task_id is None:
        return False
    
    task = manager.get_task_by_id(task_id)
    if not task:
        console.print(f"[bold red]Task {task_id} not found.[/]")
        return False
    
    new_title = Prompt.ask(
        f"[bold cyan]New title (current: '{task.title}', Enter to skip)[/]",
        default=task.title
    ).strip()
    
    new_description = Prompt.ask(
        f"[bold cyan]New description (current: '{task.description}', Enter to skip)[/]",
        default=task.description
    ).strip()
    
    try:
        success = manager.update_task(task_id, new_title, new_description)
        if success:
            console.print(Panel(f"[green]Task {task_id} updated successfully.[/]", border_style=SUCCESS_STYLE))
            return True
        else:
            console.print(f"[bold red]Failed to update task {task_id}.[/]")
            return False
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/]")
        return False

def delete_task_cli(manager: TodoManager) -> bool:
    """Handle delete with confirmation."""
    task_id = get_task_id()
    if task_id is None:
        return False
    
    if not manager.get_task_by_id(task_id):
        console.print(f"[bold red]Task {task_id} not found.[/]")
        return False
    
    if not confirm_action(f"delete task {task_id}"):
        console.print("[yellow]Deletion cancelled.[/]")
        return False
    
    try:
        success = manager.delete_task(task_id)
        if success:
            console.print(Panel(f"[green]Task {task_id} deleted successfully.[/]", border_style=SUCCESS_STYLE))
            return True
        else:
            console.print(f"[bold red]Failed to delete task {task_id}.[/]")
            return False
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/]")
        return False