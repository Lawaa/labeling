class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append({"name": task_name, "completed": False})
        print(f"Task '{task_name}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        
        print("\n--- Current Tasks ---")
        for i, task in enumerate(self.tasks):
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{i + 1}. {status} {task['name']}")
        print("---------------------\n")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"Task {task_index + 1} marked as completed.")
        else:
            print("Error: Invalid task number.")

if __name__ == "__main__":
    # Simple Testing
    manager = TaskManager()
    manager.add_task("Set up GitHub repository")
    manager.add_task("Write prompt for Model A and B")
    manager.view_tasks()
    manager.complete_task(0)
    manager.view_tasks()