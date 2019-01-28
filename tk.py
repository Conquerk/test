from tkinter import   *
top = Tk()
hello = Label(top,text='你好')
hello.pack()
quit = Button(top,text='1',command=top.quit,
bg='white',fg='black')
quit.pack(fill=X,expand=1)
mainloop()