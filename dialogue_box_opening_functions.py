#Module list_______________________________________________________________________________________________________________
from tkinter import END
from variables import list_of_skills
from variables import privacy_statment
from tkinter import Scrollbar
from tkinter import Listbox
from tkinter import RIGHT
from tkinter import LEFT
from tkinter import BOTH
from tkinter import Y
from tkinter import Tk
from tkinter import Canvas


#Open a new window with list of skills__________________________________________________________________________________________________
#This code block opens a new window with a list of skills, each with a number assigned to it. The block uses tkinter to create the new window.

def open_skilldatabase_window():
    new_window = Tk()
    new_window.title("Skill Database")
    new_window.geometry("500x500")
    scrollbar = Scrollbar(new_window)
    scrollbar.pack(side = RIGHT, fill = Y)
    mylist = Listbox(new_window, yscrollcommand = scrollbar.set )
    line_counter = 0
    for item in list_of_skills:
        line_counter = line_counter + 1
        mylist.insert(END, item + ": " + str(line_counter))
    mylist.pack(side = LEFT, fill = BOTH)
    scrollbar.config(command = mylist.yview)
    new_window.mainloop() 


#Show privacy statement in a new window_________________________________________________________________________________________________
#This block opens a new window with a privacy statement for the user.

def open_privacystatement_window():
    new_window = Tk()
    new_window.title("Our Privacy Statement")
    canvas = Canvas(new_window, width= 1000, height= 750, bg="White")
    canvas.create_text(500, 505, text=f"{privacy_statment}", fill="black", font=('Helvetica 11'))
    canvas.pack()
    scrollbar = Scrollbar(new_window)
    scrollbar.pack(side = RIGHT, fill = Y)
    mylist = Listbox(new_window, yscrollcommand = scrollbar.set )
    mylist.insert(END, privacy_statment)
    scrollbar.config(command = mylist.yview)
    new_window.mainloop() 

