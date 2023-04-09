from tkinter import *
from tkinter import ttk
from tkinter import font as tkfont


class EisenhowerMatrix:
    def __init__(self, master):
        self.master = master
        master.title("Eisenhower Matrix")

        # Define grid layout
        self.grid = Frame(master)
        self.grid.grid(row=0, column=0, sticky=N+S+E+W)

        # Define task list
        self.tasks = []

        # Create matrix labels
        important_urgent_label = Label(self.grid, text="Important / Urgent")
        important_urgent_label.grid(row=0, column=1, padx=10, pady=10)
        important_not_urgent_label = Label(self.grid, text="Important / Not Urgent")
        important_not_urgent_label.grid(row=0, column=2, padx=10, pady=10)
        not_important_urgent_label = Label(self.grid, text="Not Important / Urgent")
        not_important_urgent_label.grid(row=1, column=0, padx=10, pady=10)
        not_important_not_urgent_label = Label(self.grid, text="Not Important / Not Urgent")
        not_important_not_urgent_label.grid(row=2, column=0, padx=10, pady=10)

        # Create task entry and add button
        self.task_entry = Entry(self.grid)
        self.task_entry.grid(row=3, column=0, columnspan=3, sticky=N+S+E+W)

        self.label_options = ["Important/Urgent", "Important/Not Urgent", "Not Important/Urgent", "Not Important/Not Urgent"]

        self.label_menu = ttk.Combobox(self.grid, values=self.label_options, state="readonly")
        self.label_menu.current(0)
        self.label_menu.grid(row=4, column=1, padx=10, pady=10)

        add_task_button = Button(self.grid, text="Add Task", command=self.add_task)
        add_task_button.grid(row=4, column=2, padx=10, pady=10)

        remove_task_button = Button(self.grid, text="Remove Task", command=self.remove_task)
        remove_task_button.grid(row=5, column=2, padx=10, pady=10)

        toggle_strikethrough_task_button = Button(self.grid, text="Strike Task", command=self.toggle_strikethrough)
        toggle_strikethrough_task_button.grid(row=6, column=2, padx=10, pady=10)

        # Create task list labels
        self.important_urgent_tasks = Label(self.grid, text=" ", bg="green")
        self.important_urgent_tasks.grid(row=1, column=1, padx=10, pady=10, sticky=N+S+E+W)

        self.important_not_urgent_tasks = Label(self.grid, text=" ", bg="yellow")
        self.important_not_urgent_tasks.grid(row=1, column=2, padx=10, pady=10, sticky=N+S+E+W)

        self.not_important_urgent_tasks = Label(self.grid, text=" ", bg="blue")
        self.not_important_urgent_tasks.grid(row=2, column=1, padx=10, pady=10, sticky=N+S+E+W)

        self.not_important_not_urgent_tasks = Label(self.grid, text=" ", bg="red")
        self.not_important_not_urgent_tasks.grid(row=2, column=2, padx=10, pady=10, sticky=N+S+E+W)

    def add_task(self):
        task_text = self.task_entry.get()
        label_text = self.label_menu.get()

        if task_text:
            # Check if task already exists
            for i, task in enumerate(self.tasks):
                if task[0] == task_text:  # fix variable name here
                    # Remove the task if it already exists
                    self.tasks.pop(i)
                    break  # exit the loop if task is found
            # Add the new task
            self.tasks.append((task_text, label_text))
            self.task_entry.delete(0, END)

            # Update task list labels
            self.important_urgent_tasks.config(text="\n".join([task[0] for task in self.tasks if task[1] == "Important/Urgent"]))
            self.important_not_urgent_tasks.config(text="\n".join([task[0] for task in self.tasks if task[1] == "Important/Not Urgent"]))
            self.not_important_urgent_tasks.config(text="\n".join([task[0] for task in self.tasks if task[1] == "Not Important/Urgent"]))
            self.not_important_not_urgent_tasks.config(text="\n".join([task[0] for task in self.tasks if task[1] == "Not Important/Not Urgent"]))

    def remove_task(self):
        task_text = self.task_entry.get()

        if task_text:
            self.tasks = [(task, label) for task, label in self.tasks if task != task_text]
            self.task_entry.delete(0, END)

            # Update task list labels
            self.important_urgent_tasks.config(text="\n".join([task[0] for task in self.tasks if task[1] == "Important/Urgent"]))
            self.important_not_urgent_tasks.config(text="\n".join([task[0] for task in self.tasks if task[1] == "Important/Not Urgent"]))
            self.not_important_urgent_tasks.config(text="\n".join([task[0] for task in self.tasks if task[1] == "Not Important/Urgent"]))
            self.not_important_not_urgent_tasks.config(text="\n".join([task[0] for task in self.tasks if task[1] == "Not Important/Not Urgent"]))


    def toggle_strikethrough(self):
        task_text = self.task_entry.get()
        if "\u0336" in task_text:  # Check if there's already a strikethrough in the text
            new_text = task_text.replace("\u0336", "")  # Remove existing strikethrough
        else:
            new_text = "\u0336".join(task_text)  # Add a strikethrough to each character in the text

        # Update task list with new task text
        for i, task in enumerate(self.tasks):
            if task[0] == task_text:
                self.tasks[i] = (new_text, task[1])
                break

        # Update task list labels
        self.important_urgent_tasks.config(text="\n".join([str(task[0]) for task in self.tasks if task[1] == "Important/Urgent"]))
        self.important_not_urgent_tasks.config(text="\n".join([str(task[0]) for task in self.tasks if task[1] == "Important/Not Urgent"]))
        self.not_important_urgent_tasks.config(text="\n".join([str(task[0]) for task in self.tasks if task[1] == "Not Important/Urgent"]))
        self.not_important_not_urgent_tasks.config(text="\n".join([str(task[0]) for task in self.tasks if task[1] == "Not Important/Not Urgent"]))

        # Update task entry with new task text
        self.task_entry.delete(0, "end")
        self.task_entry.insert(0, new_text)

root = Tk()
eisenhower_matrix = EisenhowerMatrix(root)
root.mainloop()