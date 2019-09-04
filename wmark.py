fileboi = "/users/alexandermoening/whirlcode/file.txt"
from PIL import Image, ImageTk
import PIL.Image

from tkinter import *
import tkinter as tk


def main(filename):
    global filething
    filething = {}

    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=1000, height=1000)

    mainroot = Tk()



    myframe = Frame(mainroot, relief=GROOVE, width=50, height=100, bd=1)
    myframe.pack()

    canvas = Canvas(myframe)
    root = Frame(canvas)
    myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
    myscrollbar2 = Scrollbar(myframe, orient="horizontal", command=canvas.xview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    canvas.configure(xscrollcommand=myscrollbar2.set)

    myscrollbar.pack(side="right", fill="y")
    myscrollbar2.pack(side="bottom", fill="x")
    canvas.pack(side="left")
    canvas.create_window((0, 0), window=root, anchor='nw')
    root.bind("<Configure>", myfunction)
    file = open(filename, "r")



    filestring = file.read()
    linelist = filestring.split("\n")

    links = {}
    lbllinecount = 0
    for i in linelist:

        i2 = i.split(",")
        if i2[0] == "lbl" or i2[0] == "label":
            lbls[i2[1]] = lbllinecount
        lbllinecount = lbllinecount + 1

    item = {}
    loadables = {}
    loadables2 = {}

    def get_str_var(name):
        return strvars[name]

    def add_str_var(name, data):
        strvars[name] = data
    run = True
    count = 0
    def load():
        global filething
        main(filething)

    while run == True:
        goto = False

        line = linelist[count]
        command = line.split(",")

        if command[0] == "text":
            item[command[1]] = Label(root,text=command[2])
            item[command[1]].pack()
        elif command[0] == "title":
            item[command[1]] = Label(root,text=command[2],font=("Times New Roman", 24))
            item[command[1]].pack()
        elif command[0] == "img":
            loadables[command[1]] = PIL.Image.open(command[2])
            loadables2[command[1]] = ImageTk.PhotoImage(loadables[command[1]])
            item[command[1]] = Label(root,image=loadables2[command[1]])
            item[command[1]].pack()

        elif command[0] == "link":
            if command[1] == "1":
                link1 = command[4]
                item[command[2]] = Button(root,text=command[3],command=lambda: main(link1))
                item[command[2]].pack()
            elif command[1] == "2":
                link2 = command[4]
                item[command[2]] = Button(root, text=command[3], command=lambda: main(link2))
                item[command[2]].pack()
            elif command[1] == "3":
                link3 = command[4]
                item[command[2]] = Button(root, text=command[3], command=lambda: main(link3))
                item[command[2]].pack()
            elif command[1] == "4":
                link4 = command[4]
                item[command[2]] = Button(root, text=command[3], command=lambda: main(link4))
                item[command[2]].pack()
            elif command[1] == "5":
                link5 = command[4]
                item[command[2]] = Button(root, text=command[3], command=lambda: main(link5))
                item[command[2]].pack()
            if command[1] == "6":
                link6 = command[4]
                item[command[2]] = Button(root,text=command[3],command=lambda: main(link6))
                item[command[2]].pack()
            elif command[1] == "7":
                link7 = command[4]
                item[command[2]] = Button(root, text=command[3], command=lambda: main(link7))
                item[command[2]].pack()
            elif command[1] == "8":
                link8 = command[4]
                item[command[2]] = Button(root, text=command[3], command=lambda: main(link8))
                item[command[2]].pack()
            elif command[1] == "9":
                link9 = command[4]
                item[command[2]] = Button(root, text=command[3], command=lambda: main(link9))
                item[command[2]].pack()
            elif command[1] == "10":
                link10 = command[4]
                item[command[2]] = Button(root, text=command[3], command=lambda: main(link10))
                item[command[2]].pack()


        elif command[0] == "run":
            main(command[1])

        elif command[0] == "end":
            run = False
            root.mainloop()
        else:
            print("error in line "+str(count) + "")
            print("command "+line+" not found")
            break


        if goto == False or run == False:
            count = count + 1

main(fileboi)