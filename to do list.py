import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To‑Do List")
        self.tasks = []

        self.entry = tk.Entry(self.root, width=40)
        self.entry.grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Add Task", width=10, command=self.add_task).grid(row=0, column=1)

        self.listbox = tk.Listbox(self.root, width=50, height=10, selectmode=tk.SINGLE)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        tk.Button(self.root, text="Delete Task", width=10, command=self.delete_task).grid(row=2, column=0, pady=5)
        tk.Button(self.root, text="Mark Complete", width=12, command=self.complete_task).grid(row=2, column=1, pady=5)

        self.root.mainloop()

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")  # based on similar basic app from OneCompiler :contentReference[oaicite:1]{index=1}

    def delete_task(self):
        sel = self.listbox.curselection()
        if sel:
            idx = sel[0]
            del self.tasks[idx]
            self.update_list()
        else:
            messagebox.showwarning("Warning", "Select a task to delete.")

    def complete_task(self):
        sel = self.listbox.curselection()
        if sel:
            idx = sel[0]
            self.tasks[idx] = f"{self.tasks[idx]} (Completed)"
            self.update_list()
        else:
            messagebox.showwarning("Warning", "Select a task to mark complete.")  # functionality inspired by PythonFlood tutorial :contentReference[oaicite:2]{index=2}

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for t in self.tasks:
            self.listbox.insert(tk.END, t)

if __name__ == "__main__":
    TodoApp()
