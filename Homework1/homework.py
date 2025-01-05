import tkinter as tk

root = tk.Tk()
root.geometry("750x750")
root.title("Homework")
root.config(background="blue")

button1 = tk.Button(root,text="I am button",bd=10,activebackground="yellow",activeforeground="red").place(x=50,y=50)
button2 = tk.Button(root,text="I am also button",bd=15,activebackground="green",bg="purple").place(x=600,y=50)
button3 = tk.Button(root,text="I am button too",bd=20,activebackground="cyan",fg="red",bg="green").place(x=50,y=600)
button4 = tk.Button(root,text="I am another button",bd=15,activebackground="red",activeforeground="blue",bg="orange").place(x=600,y=600)

root.mainloop()