import json
import os

class ToDoManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []   # 🔥 yahi line missing thi
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, title):
        task = {"id": len(self.tasks) + 1, "title": title, "done": False}
        self.tasks.append(task)
        self.save_tasks()
        print("✅ Task added successfully!")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        for task in self.tasks:
            status = "✔" if task["done"] else "❌"
            print(f"{task['id']}. {task['title']} [{status}]")

    def mark_done(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                self.save_tasks()
                print("✅ Task marked as done!")
                return
        print("❌ Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        self.save_tasks()
        print("🗑 Task deleted!")

def main():
    todo = ToDoManager()

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            todo.add_task(title)
        elif choice == "2":
            todo.list_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to mark done: "))
            todo.mark_done(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            todo.delete_task(task_id)
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("⚠ Invalid choice, try again.")

if __name__ == "__main__":
    main()