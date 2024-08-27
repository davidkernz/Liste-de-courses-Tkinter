from tkinter import *

screen = Tk ()

screen.title("Liste de courses")
screen.geometry("400x650+400+100")
screen.resizable(False, False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END, task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete( ANCHOR)

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readline()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file = open('tasklist.txt', 'w')
        file.close

#icon
Image_icon = PhotoImage(file="img/list.png")
screen.iconphoto(False, Image_icon)

#topbar
TopImage = PhotoImage(file="img/topbar.png")
Label(screen,image=TopImage).pack()

menuImage = PhotoImage(file="img/menu.png")
Label(screen,image=menuImage, bg="#32405b").place(x=30, y=25)

noteImage = PhotoImage(file="img/list.png")
Label(screen,image=noteImage, bg="#32405b").place(x=340, y=25)

heading = Label(screen,text="Liste de courses", font="arial 20 bold", bg="#32405b")
heading.place(x=100, y=20)

#main
frame = Frame(screen,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

addData = PhotoImage(file="img/add.png")
button = Button(frame, image=addData, bg="#32405b", bd=0, command=addTask)
button.place(x=350, y=10)

#listbox
frame1 = Frame(screen, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1, font=("arial", 12),width=40, height=16, bg="#32405b", fg="white", cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#delete
delete_img = PhotoImage(file="img/delete.png")
btn_delete = Button(screen,image=delete_img,bd=0, command=deleteTask)
btn_delete.pack(side=BOTTOM, pady=13)

#appel
openTaskFile()

screen.mainloop()