import tkinter as tk
from datetime import datetime


FILE_NAME = "tasks.txt"


def load_tasks():
    tasks = []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                name, date_str = line.split(";")

                task_date = datetime.strptime(
                    date_str,
                    "%Y-%m-%d"
                ).date()

                tasks.append((name, task_date))

    except FileNotFoundError:
        print(f"Файл {FILE_NAME} не найден")

    return tasks


def get_task_info(task_date):
    today = datetime.now().date()
    delta = (task_date - today).days

    if delta < 0:
        text = f"Прошло {-delta} дней"
        color = "red"

    elif delta == 0:
        text = "Прямо сейчас происходит"
        color = "orange"

    else:
        text = f"Осталось {delta} дней"
        color = "light blue"

    return text, color


def create_window():
    root = tk.Tk()

    root.title("Что мне делать, как мне жить?")
    root.geometry("800x500")
    root.configure(bg="black")

    title = tk.Label(
        root,
        text="Мои текущие задачи",
        font=("Times New Roman", 28, "bold", "underline"),
        fg="yellow",
        bg="black"
    )

    title.pack(pady=20)

    tasks = load_tasks()

    for name, task_date in tasks:
        text, color = get_task_info(task_date)

        label = tk.Label(
            root,
            text=f"{text} до {name}",
            font=("Arial", 18),
            fg=color,
            bg="black",
            anchor="w"
        )

        label.pack(fill="x", padx=80, pady=2)

    root.mainloop()


if __name__ == "__main__":
    create_window()