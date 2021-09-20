from tkinter import *

root=Tk()

#All the labels formed here
label1 = Label(root, text = "Julie's Party Hire List")
label2 = Label(root, text = "Customer Name")
label3 = Label(root, text = "Receipt Number")
label4 = Label(root, text = "Item Hired")
label5 = Label(root, text = "Number of Items")
label6 = Label(root, text = "Row Number")








#labels placed on the grid
label1.grid(column=1, row=0, columnspan=2)
label2.grid(column=0, row=1)
label3.grid(column=0, row=2)
label4.grid(column=0, row=3)
label5.grid(column=0, row=4)
label6.grid(column=0, row=5)





root.mainloop()
