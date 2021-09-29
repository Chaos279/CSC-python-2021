      ########################################################################
###This program is so we know who has how much of Party Hire Stuff from the store###
      ########################################################################

from tkinter import *

root=Tk()

#All the labels formed here
label1 = Label(root, text = "Julie's Party Hire List")
label2 = Label(root, text = "Customer Name")
label3 = Label(root, text = "Receipt Number")
label4 = Label(root, text = "Item Hired")
label5 = Label(root, text = "Number of Items")
label6 = Label(root, text = "Row Number")


label7 = Label(root, text="  |  Row  |  ")
label8 = Label(root, text="  |  Customer Names  |  ")
label9 = Label(root, text="  |  Reciept Number  |  ")
label10 = Label(root,text="  |  Item Hired  |  ")
label11 = Label(root,text="  |  Number of Items  |  ")


#All the entry fields
entry1 = Entry(root, width="40")
entry2 = Entry(root, width="40")
entry3 = Entry(root, width="40")
entry4 = Entry(root, width="40")
entry5 = Entry(root, width="40")

#Buttons labeled here
button1 = Button(root, text="Save", padx = 30, pady = 10)
button2 = Button(root, text="Delete", padx = 20, pady = 10)
button3 = Button(root, text="Exit", padx = 30, pady = 10, command = quit)













#Button commands

def quit(): #code for button3 to leave code
    root.destroy.pack()


def save():  # the save button
    
        




 











#labels placed on the grid
label1.grid(column=1, row=0, columnspan=3)
label2.grid(column=0, row=1)
label3.grid(column=0, row=2)
label4.grid(column=0, row=3)
label5.grid(column=0, row=4)
label6.grid(column=0, row=5)

label7.grid(column=0, row=8)
label8.grid(column=1, row=8)
label9.grid(column=2, row=8)
label10.grid(column=3, row=8)
label11.grid(column=4, row=8)

# Entry field positions
entry1.grid(column=1, row=1, columnspan=3)
entry2.grid(column=1, row=2, columnspan=3)
entry3.grid(column=1, row=3, columnspan=3)
entry4.grid(column=1, row=4, columnspan=3)
entry5.grid(column=1, row=5, columnspan=3)

#Button positions
button1.grid(column=0, row=7)
button2.grid(column=2, row=7)
button3.grid(column=4, row=7)



root.mainloop()
