# import everything from tkinter
from tkinter import *
import backendtest  # Attach the backend to the frontend of the program


# Create a window object
window = Tk()
window.wm_title('FoodBev')


def view_command():
    list1.delete(0, END)
    for row in backendtest.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backendtest.search(ProductType_Text.get(), ProcessDesc_Text.get()):
        list1.insert(END, row)


#The selected row should automatically fill in the empty entries

def get_selected_row(event):
    global selected_turple
    index=list1.curselection()[0]
    selected_turple=list1.get(index)
    new_selected_turple = selected_turple.split(",")
    e1.delete(0,END)
    e1.insert(END,new_selected_turple[0])
    e2.delete(0,END)
    e2.insert(END,new_selected_turple[1])
    e3.delete(0,END)
    e3.insert(END,new_selected_turple[2])
    e4.delete(0,END)
    e4.insert(END,new_selected_turple[3])
    e5.delete(0,END)
    e5.insert(END,new_selected_turple[4])
    e6.delete(0,END)
    e6.insert(END,new_selected_turple[5])
    #print(type(new_selected_turple))


# define tabs i.e column names from your db
l1 = Label(window, text="Product Type")
l1.grid(row=0, column=0)

l2 = Label(window, text="Process Desc")
l2.grid(row=0, column=3)

l3 = Label(window, text="Temperature")
l3.grid(row=1, column=0)

l4 = Label(window, text="Pressure")
l4.grid(row=1, column=3)

l5 = Label(window, text="ERP System")
l5.grid(row=2, column=0)

l6 = Label(window, text="MES")
l6.grid(row=2, column=3)

# define entries
ProductType_Text = StringVar()
e1 = Entry(window, textvariable=ProductType_Text)
e1.grid(row=0, column=1)

ProcessDesc_Text = StringVar()
e2 = Entry(window, textvariable=ProcessDesc_Text, width=22)
e2.grid(row=0, column=4, columnspan=2)

Temperature_Text = StringVar()
e3 = Entry(window, textvariable=Temperature_Text)
e3.grid(row=1, column=1)

Pressure_Text = StringVar()
e4 = Entry(window, textvariable=Pressure_Text, width=22)
e4.grid(row=1, column=4, columnspan=2)


ERP_Text = StringVar()
e5 = Entry(window, textvariable=ERP_Text)
e5.grid(row=2, column=1)

MES_Text = StringVar()
e6 = Entry(window, textvariable=MES_Text, width=22)
e6.grid(row=2, column=4, columnspan=2 )

# define listBox
list1 = Listbox(window, height=25, width=65)
list1.grid(row=5, column=1, rowspan=4)

list2 = Listbox(window, height=25, width=65)
list2.grid(row=5, column=5, rowspan=4)

# Attach scrollbar to the list
sb1 = Scrollbar(window)
sb1.grid(row=3, column=3, rowspan=6)

#bind method
list1.bind("<<ListboxSelect>>", get_selected_row)

#sb2 = Scrollbar(window)
# sb2.grid(row=4,column=2,columnspan=6)

# Apply the scrollbar to list box
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# list1.configure(xscrollcommand=sb2.set)
# sb2.configure(command=list1.xview)

# define Buttons
b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=5, column=0)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=6, column=0)

#b3= Button(window, text="Add Entry", width=12)
#b3.grid(row=4, column=3)

#b4= Button(window, text="Update selected", width=12)
#b4.grid(row=5, column=3)

#b5= Button(window, text="Delete selected", width=12)
#b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=0)

b7 = Button(window, text= "KeyWord Search", width=12)
b7.grid(row=6, column=6)


# Allows the build window to remain active until the user decides to close it
window.mainloop()
