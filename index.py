from tkinter import *

root=Tk()

#All the labels formed here
label1 = Label(root, text = "Julie's Party Hire List")
label2 = Label(root, text = "Customer Name")
label3 = Label(root, text = "Receipt Number")
label4 = Label(root, text = "Item Hired")
label5 = Label(root, text = "Number of Items")
label6 = Label(root, text = "Row Number")

#All the entry fields
entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)

#Buttons labeled here
button1 = Button(root, text="Save", padx = 30, pady = 10)
button2 = Button(root, text="Delete")
button3 = Button(root, text="Exit", command = quit)



#Button commands

def quit():
    root.destroy.pack()








 











#labels placed on the grid
label1.grid(column=1, row=0, columnspan=3)
label2.grid(column=0, row=1)
label3.grid(column=0, row=2)
label4.grid(column=0, row=3)
label5.grid(column=0, row=4)
label6.grid(column=0, row=6)


# Entry field positions
entry1.grid(column=1, row=1, columnspan=2)
entry2.grid(column=1, row=2, columnspan=2)
entry3.grid(column=1, row=4, columnspan=2)
entry4.grid(column=1, row=6)

#Button positions
button1.grid(column=3, row=1, rowspan=4)
button2.grid(column=3, row=6)
button3.grid(column=3, row=7)



root.mainloop()
