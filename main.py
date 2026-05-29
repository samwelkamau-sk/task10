from task_manager import task_utils

def main():
    while True:
        print("\n--- Task Management System ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            t = input("Title: ")
            d = input("Description: ")
            date = input("Due Date (YYYY-MM-DD): ")
            if task_utils.add_task(t, d, date):
                print("Task added successfully!")
            else:
                print("Error: Invalid task details.")
                
        elif choice == "2":
            idx = int(input("Enter task index: "))
            if task_utils.mark_task_as_complete(idx):
                print("Task marked as complete!")
            else:
                print("Invalid index.")
                
        elif choice == "3":
            task_utils.view_pending_tasks()
            
        elif choice == "4":
            print(f"Progress: {task_utils.calculate_progress()}%")
            
        elif choice == "5":
            break

if __name__ == "__main__":
    main()