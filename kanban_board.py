from tkinter import * 

def create_task(event):
    task = entry.get()
    if task:
        todo_list.insert(END, task)
        entry.delete(0,END)

def move_task(event, source_list, target_list):
    shift = source_list.get(source_list.curselection())
    source_list.delete(source_list.curselection())
    target_list.insert(END, shift)

def delete_task(event):
    todo_list.delete(0,END)
    in_progress_list.delete(0,END)
    done_list.delete(0,END)
        
root = Tk()
root.title('Kanban Board')

todo_list = Listbox(root, height=10, width=30)
in_progress_list = Listbox(root, height=10, width=30)
done_list = Listbox(root, height=10, width=30)

todo_list.grid(row=0, column=0, padx=10, pady=10)
in_progress_list.grid(row=0, column=1, padx=10, pady=10)
done_list.grid(row=0, column=2, padx=10, pady=10)

add_label = Label(root, text='Add text: ')
add_label.grid(row=1, column=0, pady=5)

entry = Entry(root, width=30)
entry.grid(row=1, column=1, pady=5)

add_button = Button(root, text='Add', width=10)
add_button.grid(row=1, column=2, pady=5)
add_button.bind('<Button-1>', create_task)

add_button = Button(root, text='Delete', width=10)
add_button.grid(row=2, column=2, pady=5)
add_button.bind('<Button-1>', delete_task)

todo_list.bind("<Double-Button-1>", lambda e: move_task(e, todo_list, in_progress_list))
in_progress_list.bind("<Double-Button-1>", lambda e: move_task(e, in_progress_list, done_list))

root.mainloop()