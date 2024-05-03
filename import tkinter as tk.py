import tkinter as tk

def ajouter_entry():
    global entry_count
    entry_count += 1
    entry = tk.Entry(root)
    entry.grid(row=entry_count, column=0, padx=10, pady=5)
    entries.append(entry)

root = tk.Tk()
root.title("Ajouter Entry")

entry_count = 0
entries = []

button = tk.Button(root, text="Ajouter Entry", command=ajouter_entry)
button.grid(row=0, column=0, padx=10, pady=5)

root.mainloop()
