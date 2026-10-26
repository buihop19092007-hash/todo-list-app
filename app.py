tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

if __name__ == "__main__":
    add_task("Learn Python")
    print("My To-Do List:")
    for task in tasks:
        print(f"- {task}")