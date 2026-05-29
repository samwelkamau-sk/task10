import task_utilis
import validation

def main():
    while True:
        # ... (Print menu) ...
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            date = input("Due Date (YYYY-MM-DD): ")
            task_utilis.add_task(title, desc, date)
        elif choice == "2":
            idx = int(input("Enter task index to complete: "))
            task_utilis.mark_task_as_complete(idx)
        elif choice == "3":
            # Logic to print pending tasks
            for i, t in enumerate(task_utilis.tasks):
                if not t["completed"]:
                    print(f"{i}: {t['title']}")
        elif choice == "4":
            print(f"Progress: {task_utilis.calculate_progress()}%")
        # ...