import tkinter
from tkinter import *


root=Tk()
root.title("To-Do List")
root.geometry("400x650+400+50")
root.resizable(False,False)

task_list = []

def deleteTask():
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)

def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)


def openTaskFile():

    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

            for task in tasks:
                if task != "\n":
                    task_list.append(task)
                    listbox.insert(END,task)

    except:
        file=open("tasklist.txt","w")
        file.close()
#header
heading=Label(root,text="Create a To-Do List!",font="arial 20 bold",fg="black")
heading.place(x=70,y=100)

#main
frame= Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font="arial 12 bold", width=6,height=2, bg="#5a95ff", fg="#fff",bd=0, command=addTask)
button.place(x=340,y=0)

#listbox

frame1=Frame(root,bd=3,width=700,height=280,bg="#d3d3d3")
frame1.pack(pady=(260,0))
listbox= Listbox(frame1,font=("arial",12),width=40,height=16,bg="#d3d3d3")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

openTaskFile()

#delete

Delete_icon=PhotoImage(file="delete.png")
Button(root,image=Delete_icon,height=80,bd=0, command=deleteTask).pack(side=BOTTOM,pady=9)

root.mainloop()