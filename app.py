

def click():
    print("YOU SAVED THIS MESSAGE!")
#create a button for saving

from tkinter import Entry, Button, Tk

def submit_button():
    username = entry.get() #when you press on the button, ....
    print(username)

window = Tk() #create a web window

entry = Entry(window, width=23) #create a user input
entry.pack(side="left")
#entry.config()

button = Button(window, text="Save", command=submit_button) #config the button 
button.pack(side="left") 
window.mainloop()




