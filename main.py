import tkinter as tk

def add1():
    addd = ent.get()
    if addd:
        lis.insert(tk.END, addd)
        ent.delete(0, tk.END)

def done():
    done1 = lis.curselection()
    if done1:
        lis.itemconfig (done1, bg="DarkOliveGreen3")

def dele():
    dele1 = lis.curselection()
    if dele1:
        lis.delete(dele1)

root = tk.Tk ()

root.title ('Задачи')
root.configure(bg='grey97')

text1 = tk.Label (root, text="Поле для ввода задач")
text1.pack (pady=10)

ent = tk.Entry (root, width=40)
ent.pack ()

but1 = tk.Button (root, text="Добавить задачу", bg="LemonChiffon2", command=add1)
but1.pack (pady=5)

but2 = tk.Button (root, text="Отметить выполненную задачу", bg="LemonChiffon2", command=done)
but2.pack (pady=5)

but3 = tk.Button (root, text="Удалить задачу", bg="LemonChiffon2", command=dele)
but3.pack (pady=5)

lis = tk.Listbox (root, height=40, width=40, bg="grey99")
lis.pack (pady=10)


root.mainloop()