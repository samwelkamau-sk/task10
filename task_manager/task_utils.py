from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    if validate_task_title(title) and validate_task_description(description) and validate_due_date(due_date):
        task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }
        tasks.append(task)
        return True
    return False

def mark_task_as_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        return True
    return False

def view_pending_tasks():
    pending = [t for t in tasks if not t["completed"]]
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i}: {task['title']} - {task['description']} (Due: {task['due_date']})")

def calculate_progress(tasks_list=None):
    source = tasks_list if tasks_list is not None else tasks
    if not source:
        return 0.0
    completed = [t for t in source if t["completed"]]
    return (len(completed) / len(source)) * 100