from tkinter import *
from tkinter import ttk
from BackEnd import *

window = Tk()
window.title("Library Management")
window.geometry('550x450')
# =================== labels =============================
l1 = Label(window, text="Book Title: ")
l1.grid(row=0, column=0)


l2 = Label(window, text="Author: ")
l2.grid(row=0, column=2)


l3 = Label(window, text="Publish Year: ")
l3.grid(row=1, column=0)


l4 = Label(window, text="Subject: ")
l4.grid(row=1, column=2)

# =================== Entries =============================
title_text = StringVar()
e1 = Entry(window, textvariable=title_text, width=30)
e1.grid(row=0, column=1)

Author_text = StringVar()
e2 = Entry(window, textvariable=Author_text, width=30)
e2.grid(row=0, column=3)

Year_text = StringVar()
e3 = Entry(window, textvariable=Year_text, width=30)
e3.grid(row=1, column=1)

Subject_text = StringVar()
e4 = Entry(window, textvariable=Subject_text, width=30)
e4.grid(row=1, column=3)
# =================== Listbox =============================
lst = Listbox(window)
lst.grid(row=2, column=0, rowspan=6, columnspan=2 , ipadx=80, ipady=100)
sco = Scrollbar(window)
sco.grid(row=2, column=2, rowspan=6)
lst.configure(yscrollcommand=sco.set)
sco.configure(command=lst.yview)
# =================== Def =============================
def clear_list():
    lst.delete(0, END)
    
def fill_list(books):
    for i in books:
        lst.insert(END,i)
    
def Show_all():
    clear_list()
    books = show_data()
    fill_list(books)
        
def Search():
    clear_list()
    books = search(title_text.get(),Author_text.get(),Year_text.get(),Subject_text.get())
    fill_list(books)
        
def Add_command():
    insert_data(title_text.get(),Author_text.get(),Year_text.get(),Subject_text.get())
    Show_all()
    
def get_select(event):
    global select
    if len(lst.curselection())>0:
        pass
    # not error
    index = lst.curselection()[0]
    select = lst.get(index)
    e1.delete(0,END)
    e1.insert(END, select[1])
    e2.delete(0,END)
    e2.insert(END, select[2])
    e3.delete(0,END)
    e3.insert(END, select[3])
    e4.delete(0,END)
    e4.insert(END, select[4])
    
lst.bind('<<ListboxSelect>>',get_select)

def Delete():
    delete_data(select[0])
    Show_all()

def Update():
    update_data(select[0],title_text.get(),Author_text.get(),Year_text.get(),Subject_text.get())
    Show_all()
# =================== Button =============================
b1 = ttk.Button(window, text="Show All", width=12 , command=lambda: Show_all())
b1.grid(row=2, column=3,pady=5 , ipadx=40 , ipady=5)

b2 = ttk.Button(window, text="New", width=12 , command=lambda : Add_command())
b2.grid(row=3, column=3,pady=5 , ipadx=40 , ipady=5)

b3 = ttk.Button(window, text="Edit", width=12 , command=lambda : Update())
b3.grid(row=4, column=3,pady=5 , ipadx=40 , ipady=5)

b5 = ttk.Button(window, text="Cancel", width=12, command=window.destroy)
b5.grid(row=5, column=3,pady=5 , ipadx=40 , ipady=5)

b6 = ttk.Button(window, text="Delete", width=12,command=lambda : Delete())
b6.grid(row=6, column=3,pady=5 , ipadx=40 , ipady=5)

b7 = ttk.Button(window, text="Search", width=12, command=lambda: Search())
b7.grid(row=7, column=3 ,padx=10 , ipadx=40 , ipady=5)

# =================== Search Books =============================
# frame_radio = LabelFrame(window, text='Search Books')
# frame_radio.grid(row = 8, column = 0, rowspan=10, columnspan=10)
# radio1 = Radiobutton(frame_radio ,text='Title',foreground='blue')
# radio1.grid(row = 0, column = 1,padx=10)

# radio1 = Radiobutton(frame_radio , text='Auther',foreground='blue')
# radio1.grid(row = 0, column = 2,padx=10)

# radio1 = Radiobutton(frame_radio , text='Year',foreground='blue')
# radio1.grid(row = 0, column = 3,padx=10)

# radio1 = Radiobutton(frame_radio , text='Subject',foreground='blue')
# radio1.grid(row = 0, column = 4,padx=10)

# e5 =  Entry(frame_radio, textvariable='Search_Books' , width=40)
# e5.grid(row=0,column=5,padx=10)

Show_all()
window.mainloop()