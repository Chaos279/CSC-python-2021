# Made by : Benedick Cruz Baskar Thangaraj
# Started : 14 / 09 / 21
# Finished : 01 / 10 / 21
# This code was made for the standards AS91896 and AS91897




      ########################################################################
###This program is so we know who has how much of Party Hire Stuff from the store###
      ########################################################################

#importing tkinter
from tkinter import *
#importing Pillow to add an image
from PIL import ImageTk,Image

#creating my screen 
root=Tk()
#Changing the title of the screen
root.title("Julie's Party Hire")




#global variables used
global item_details, entry1, entry2, entry3, entry4, entry5, total_entries, row_count
total_entries = 0
item_details = []
row_count = 0


#Button commands

def print(): #print camp details
    #global variables used
    global item_details, entry1, entry2, entry3, entry4, entry5, total_entries, row_count
    

    #checks the info stored on the item_details list and then places them on the grid
    while row_count < total_entries :
            Label(root, text=row_count).grid(column=0,row=row_count+9) 
            Label(root, text="                            "+(item_details[row_count][0])+"                            ").grid(column=1,row=row_count+9)
            Label(root, text="                            "+(item_details[row_count][1])+"                            ").grid(column=2,row=row_count+9)
            Label(root, text="                            "+(item_details[row_count][2])+"                            ").grid(column=3,row=row_count+9)
            Label(root, text="                            "+(item_details[row_count][3])+"                            ").grid(column=4,row=row_count+9)
            row_count +=  1 #adds a row so the next print goes on the following line


def quit(): #code for button# to leave the screen/root
    root.destroy()#destroys root

 
def check(data, data_type): #function used to check if the entered value is an integer
    try:
        data_type(data)
        return True
    except ValueError:
        return False            

def append():  # add next item to the list
    #global variables used
    global item_details, entry1, entry2, entry3, entry4, entry5, total_entries, row_count, error1, error2, error3

    #checking all the requirements
    if len(entry1.get()) !=0 and len(entry2.get()) !=0 and len(entry3.get()) !=0 and len(entry4.get()) !=0 and check(entry2.get(), int) and check(entry4.get(), int):

        #checking if the items hired is between 1 and 500
        if 1 <= int(entry4.get()) <= 500:

            #storing the list into item_details
            item_details.append([entry1.get(),entry2.get(),entry3.get(),entry4.get()])

            #emptying all the entry fields
            entry1.delete(0,'end')
            entry2.delete(0,'end')
            entry3.delete(0,'end')
            entry4.delete(0,'end')
            total_entries +=  1

            #destroying any error messages
            for obj in root.grid_slaves(row=4, column=4):
                obj.destroy()

            for obj in root.grid_slaves(row=2, column=4):
                obj.destroy()

        else:

            #destroying any error messages
            for obj in root.grid_slaves(row=4, column=4):
                obj.destroy()
            for obj in root.grid_slaves(row=2, column=4):
                obj.destroy()

            #error message if item hired is not between 1 and 500
            error1 = Label(root, text="Enter a number between 1 and 500", fg="red").grid(column=4, row=4)
            

    else :

        #destroying any error messages
        for obj in root.grid_slaves(row=4, column=4):
                obj.destroy()
        for obj in root.grid_slaves(row=2, column=4):
                obj.destroy()

        #error message if receipt number and items hired entered values are not integers
        error2 = Label(root, text="Only Numbers", fg="red").grid(column=4, row=2)
        error1 = Label(root, text="Only Numbers", fg="red").grid(column=4, row=4)


def delete():


    #global values used
    global item_details, entry1, entry2, entry3, entry4, entry5, total_entries, row_count, error1, error2, error3
    #find which row is to be deleted and delete it
    if entry5.get() == "":

            #destroying any error messages
            for obj in root.grid_slaves(row=5, column=4):
                obj.destroy()

            #error message if there is no value in row number
            error3 = Label(root, text="Please enter a row number", fg="red").grid(column=4, row=5)

    elif check(entry5.get(), int):

        if int(entry5.get()) > row_count:
            
            #destroying any error messages
            for obj in root.grid_slaves(row=5, column=4):
                    obj.destroy()

                    # error message if the value entered in row number does not exist
                    error3 = Label(root, text="Please enter a valid number", fg="red").grid(column=4, row=5)

        else:

            #destroying any error messages
            for obj in root.grid_slaves(row=5, column=4):
                    obj.destroy()
                    
            del item_details[int(entry5.get())]
            total_entries = total_entries - 1
            entry5.delete(0,'end')
            #clear the last item displayed on the GUI
            Label(root, text="                                  ").grid(column=0,row=row_count+8) 
            Label(root, text="                                  ").grid(column=1,row=row_count+8)
            Label(root, text="                                  ").grid(column=2,row=row_count+8)
            Label(root, text="                                  ").grid(column=3,row=row_count+8)
            Label(root, text="                                  ").grid(column=4,row=row_count+8)
            #print all the items in the list
            print()

    
    else:
            #destroying any error messages
            for obj in root.grid_slaves(row=5, column=4):
                obj.destroy()

                #error message if the value entered in row number is not an integer
                error3 = Label(root, text="Please enter a number", fg="red").grid(column=4, row=5)


#adding an image next to the title label for aesthetics
my_img = ImageTk.PhotoImage(Image.open("balloon1.jpg")) # link for the image --> https://i.ebayimg.com/thumbs/images/g/OigAAOSwuTldtvxx/s-l96.jpg
my_label = Label(image=my_img, width=50, height=75)#placing the image on a label
my_label.grid(row=0, column=0)#placing the label with the image on root/screen

#All the labels formed here
label_title = Label(root, text = "Julie's Party Hire", font="serif 35 bold")
label_name = Label(root, text = "Customer Name", font="serif 10 bold")
label_receipt = Label(root, text = "Receipt Number", font="serif 10 bold")
label_item = Label(root, text = "Item Hired", font="serif 10 bold")
label_itemno = Label(root, text = "Number of Items", font="serif 10 bold")
label_rowno = Label(root, text = "Row Number", font="serif 10 bold")


label7 = Label(root, text="  |  Row  |  ", font="serif 10 italic")
label8 = Label(root, text="  |  Customer Names  |  ", font="serif 10 italic")
label9 = Label(root, text="  |  Reciept Number  |  ", font="serif 10 italic")
label10 = Label(root,text="  |  Item Hired  |  ", font="serif 10 italic")
label0 = Label(root,text="  |  Number of Items  |  ", font="serif 10 italic")


#All the entry fields on the grid
entry1 = Entry(root, width="40")#customer name
entry2 = Entry(root, width="40")#receipt number
entry3 = Entry(root, width="40")#item hired
entry4 = Entry(root, width="40")#number of items
entry5 = Entry(root, width="40")#row number

#Buttons placed here
button1 = Button(root, text="Append Details", padx = 15, pady = 10, command = append, bg="green")
button2 = Button(root, text="Print Row", padx = 25, pady = 10, command = print, bg="green")
button3 = Button(root, text="Delete Row", padx = 20, pady = 10, command = delete, bg="red")
button4 = Button(root, text="Exit", padx = 30, pady = 10, command = quit, fg="red")






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
