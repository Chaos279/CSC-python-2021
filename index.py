      ########################################################################
###This program is so we know who has how much of Party Hire Stuff from the store###
      ########################################################################

from tkinter import *

root=Tk()

#global variables used
global item_details, entry1, entry2, entry3, entry4, entry5, total_entries, row_count
total_entries = 0
item_details = []
row_count = 0

#Button commands

def print(): #print camp details
    global item_details, entry1, entry2, entry3, entry4, entry5, total_entries, row_count
    while row_count < total_entries :
            Label(root, text=row_count).grid(column=0,row=row_count+9) 
            Label(root, text=(item_details[row_count][0])).grid(column=1,row=row_count+9)
            Label(root, text=(item_details[row_count][1])).grid(column=2,row=row_count+9)
            Label(root, text=(item_details[row_count][2])).grid(column=3,row=row_count+9)
            Label(root, text=(item_details[row_count][3])).grid(column=4,row=row_count+9)
            row_count +=  1


    

def quit(): #code for button3 to leave code
    root.destroy()





 
def check(data, data_type): #code used to check if the entered value is an integer
    try:
        data_type(data)
        return True
    except ValueError:
        return False            

def append():  # add next item to the list
    global item_details, entry1, entry2, entry3, entry4, entry5, total_entries, row_count, error1, error2
    #global variables used
    if len(entry1.get()) !=1 and len(entry2.get()) !=1 and len(entry3.get()) !=1 and len(entry4.get()) !=1 and check(entry2.get(), int) and check(entry4.get(), int):

        if 1 <= int(entry4.get()) <= 500:
        
            item_details.append([entry1.get(),entry2.get(),entry3.get(),entry4.get()])
            entry1.delete(0,'end')
            entry2.delete(0,'end')
            entry3.delete(0,'end')
            entry4.delete(0,'end')
            total_entries +=  1

            for obj in root.grid_slaves(row=4, column=4):
                obj.destroy()

            for obj in root.grid_slaves(row=2, column=4):
                obj.destroy()

        else:
            for obj in root.grid_slaves(row=4, column=4):
                obj.destroy()
            for obj in root.grid_slaves(row=2, column=4):
                obj.destroy()
                
            error1 = Label(root, text="Enter a number between 1 and 500", fg="red").grid(column=4, row=4)
            

    else :

        for obj in root.grid_slaves(row=4, column=4):
                obj.destroy()
        for obj in root.grid_slaves(row=2, column=4):
                obj.destroy()
                
        error2 = Label(root, text="Only Numbers", fg="red").grid(column=4, row=2)
        error1 = Label(root, text="Only Numbers", fg="red").grid(column=4, row=4)


    

#All the labels formed here
label_title = Label(root, text = "Julie's Party Hire")
label_name = Label(root, text = "Customer Name")
label_receipt = Label(root, text = "Receipt Number")
label_item = Label(root, text = "Item Hired")
label_itemno = Label(root, text = "Number of Items")
label_rowno = Label(root, text = "Row Number")


label7 = Label(root, text="  |  Row  |  ")
label8 = Label(root, text="  |  Customer Names  |  ")
label9 = Label(root, text="  |  Reciept Number  |  ")
label10 = Label(root,text="  |  Item Hired  |  ")
label0 = Label(root,text="  |  Number of Items  |  ")


#All the entry fields
entry1 = Entry(root, width="40")
entry2 = Entry(root, width="40")
entry3 = Entry(root, width="40")
entry4 = Entry(root, width="40")
entry5 = Entry(root, width="40")

#Buttons placed here
button1 = Button(root, text="Append", padx = 30, pady = 10, command = append)
button2 = Button(root, text="Print", padx = 30, pady = 10, command = print)
button3 = Button(root, text="Delete", padx = 20, pady = 10)
button4 = Button(root, text="Exit", padx = 30, pady = 10, command = quit)






#labels placed on the grid
label_title.grid(column=1, row=0, columnspan=3)
label_name.grid(column=0, row=1)
label_receipt.grid(column=0, row=2)
label_item.grid(column=0, row=3)
label_itemno.grid(column=0, row=4)
label_rowno.grid(column=0, row=5)

label7.grid(column=0, row=8)
label8.grid(column=1, row=8)
label9.grid(column=2, row=8)
label10.grid(column=3, row=8)
label0.grid(column=4, row=8)

# Entry field placed on the grid
entry1.grid(column=1, row=1, columnspan=3)
entry2.grid(column=1, row=2, columnspan=3)
entry3.grid(column=1, row=3, columnspan=3)
entry4.grid(column=1, row=4, columnspan=3)
entry5.grid(column=1, row=5, columnspan=3)

#Button placed on the grid
button1.grid(column=0, row=7)
button2.grid(column=1, row=7)
button3.grid(column=2, row=7)
button4.grid(column=4, row=7)



root.mainloop()
