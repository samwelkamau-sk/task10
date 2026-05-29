from validation import validate_task_title, validate_due_date

tasks = []

def add_task(title, description, due_date):
    if validate_task_title(title) and validate_due_date(due_date):
        new_task = {"title": title, "description": description, "due_date": due_date, "completed": False}
        tasks.append(new_task)
    else:
        print("Invalid input!")

def mark_task_as_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
    else:
        print("Invalid index.")

def calculate_progress():
    if not tasks: return 0
    completed = [t for t in tasks if t["completed"]]
    return (len(completed) / len(tasks)) * 100