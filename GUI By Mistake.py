from tkinter import *

window = Tk()

# Configure
window.configure(bg="aqua")

# Geometry
window.geometry("500x500")

# Window Title
window.title("Telephone Directory")

# Title
Label(text="Telephone Directory", bg="grey", width="500").pack()

#Declaring Variables

UserName_Var = StringVar()
UserName_Num = StringVar()

SearchUser_Var = StringVar()

#Previous Code

f = open("Directory.txt", "a")

def Save():
    global f
    f = open("Directory.txt", "a")
    f.write(f"Name : {UserName_Var.get()}, Number : {UserName_Num.get()}. \n")
    f.close()
    newWindow.destroy()


def PrintLines(x):
    global lines
    f=open('Directory.txt')
    lines=f.readlines()
    print(lines[x])

def FindUserName():
    f = open('Directory.txt','r')
    line_num = 0
    search_phrase = str(SearchUser_Var.get())
    for line in f.readlines():
        line_num += 1
        if line.find(search_phrase) >= 0:
            # print(line_num)
            PrintLines(int(line_num - 1))

            Label(newWindow, text=lines[line_num - 1], bg="green").pack()

#Definations

def AddANewEntry():
    global UserName, UserNumber, newWindow
    newWindow = Toplevel(window)
    newWindow.title("Add An Entry")
    newWindow.geometry("500x500")
    newWindow.configure(bg="orange")
    Label(newWindow, text="Add An Entry", bg="grey", width="500").pack()

    Label(newWindow, text="", bg="orange").pack()
    Label(newWindow, text="", bg="orange").pack()
    Label(newWindow, text="", bg="orange").pack()
    Label(newWindow, text="", bg="orange").pack()

    Label(newWindow, text="Enter The Name", bg="orange").pack()

    UserName = Entry(newWindow, width= 40, textvariable=UserName_Var).pack()

    Label(newWindow, text="", bg="orange").pack()
    Label(newWindow, text="", bg="orange").pack()
    Label(newWindow, text="", bg="orange").pack()
    Label(newWindow, text="", bg="orange").pack()
    Label(newWindow, text="", bg="orange").pack()
    Label(newWindow, text="", bg="orange").pack()

    Label(newWindow, text="Enter The Number", bg="orange").pack()

    UserNumber = Entry(newWindow, width= 40, textvariable=UserName_Num).pack()

    Label(newWindow, text="", bg="orange").pack()
    Label(newWindow, text="", bg="orange").pack()
    Label(newWindow, text="", bg="orange").pack()

    Button(newWindow, text="Save", width=50,height=4, bg="black", fg="white", command=Save).pack()

#Search For Existing Entry

def SearchContact():
    global UserName, UserNumber, newWindow
    newWindow = Toplevel(window)
    newWindow.title("Search For An Existing Contact")
    newWindow.geometry("500x500")
    newWindow.configure(bg="green")
    Label(newWindow, text="Search For An Existing Contact", bg="grey", width="500").pack()

    Label(newWindow, text="", bg="green").pack()
    Label(newWindow, text="", bg="green").pack()
    Label(newWindow, text="", bg="green").pack()
    Label(newWindow, text="", bg="green").pack()
    
    Label(newWindow, text="Enter The Name Of The Contact", bg="green").pack()

    Entry(newWindow, width= 40, textvariable=SearchUser_Var).pack()
    
    Label(newWindow, text="", bg="green").pack()
    Label(newWindow, text="", bg="green").pack()
    Label(newWindow, text="", bg="green").pack()
    Label(newWindow, text="", bg="green").pack()
    Label(newWindow, text="", bg="green").pack()
    Label(newWindow, text="", bg="green").pack()

    Button(newWindow, text="Search", width=50,height=4, bg="black", fg="white", command=FindUserName).pack()

    Label(newWindow, text="", bg="green").pack()
    Label(newWindow, text="", bg="green").pack()

# Leaving Blank Place

Label(text="", bg="aqua").pack()
Label(text="", bg="aqua").pack()
Label(text="", bg="aqua").pack()
Label(text="", bg="aqua").pack()

button1 =  Button(window, text="Add A New Entry", width=50,height=4, bg="black", fg="white", command    =AddANewEntry).pack()

#Adding Some Blank Space

Label(text="", bg="aqua").pack()
Label(text="", bg="aqua").pack()
Label(text="", bg="aqua").pack()
Label(text="", bg="aqua").pack()
Label(text="", bg="aqua").pack()
Label(text="", bg="aqua").pack()
Label(text="", bg="aqua").pack()
Label(text="", bg="aqua").pack()

button2 =  Button(window, text="Search For an Existing Entry", width=50,height=4, bg = "black", fg = "white",command=SearchContact).pack()

window.mainloop()