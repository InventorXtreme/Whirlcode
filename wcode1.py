import os
import sys
global com
global prgm
global bob
global vardict
vardict = {}
com = 0
bob = 0
filename = "/users/alexandermoening/whirlcode/file.txt"
name = filename
def open_text(name):
    global text
    global pgrm
    global com
    global vardict

    f = open(name, "rU")
    pgrm=f.read().replace('\n', '')
    f.close()
def loadr(filenamel):
    global bob
    open_text(filenamel)
    bob = 0
def interperit(command):
    global bob
    global text
    global filename
    global autosave
    global com
    command_list = command.split(",")

    if command_list[0] == "change":
        try: text[int(command_list[1])] = command_list[2][1:]
        except: print("\tCommand either missing arguments or one of the arguments are out of range")
    elif command_list[0] == "open":
        if len(command_list) > 1:
            filename = command_list[1][1:]
            open_text(filename)
        else:
            open_text()
    elif command_list[0] == "save":
        if(len(command_list) > 1):
            save_text(command_list[1][1:])
        else:
            save_text()
    elif command_list[0] == "autosave":
        if autosave:
            autosave = False
            print("\tAutosave disabled")
        else:
            autosave = True
            print("\tAutosave enabled")
    elif command_list[0] == "new":
        filename = command_list[1][1:]
        save_text(command_list[1])
        text[:] = []
    elif command_list[0] == "print":
        if len(command_list) > 1:
            print(text[int(command_list[1])])
        else:
            print_text()
    elif command_list[0] == "nl" or command_list[0] == r"\n" or command_list[0] == "new line":
        if len(command_list) > 2:
            text.insert(int(command_list[1]), command_list[2][1:])
        else:
            text.append(command_list[1][1:])
    elif command_list[0] == "find":
        for b in range(0, len(text)):
            if text[b].find(command_list[1][1:]) != -1:
                print("    ", b, text[b])
    elif command_list[0] == "clear": os.system("cls")
    elif command_list[0] == "remove":
        for b in range(0, len(text)):
            if not len(command_list) > 2:
                text[b] = text[b].replace(command_list[1][1:], "")
            else:
                text[b] = text[b].replace(command_list[1][1:], command_list[2][1:])
    elif command_list[0] == "load":
        try:
            f = open(command_list[1][1:] + ".py", "r")
            f.close
            loaded.append(command_list[1][1:])
        except: print("\tCouldn't load " + command_list[1] + ",\n\t\tPlugin does not exist")
        print(loaded)
    elif command_list[0] == "A":
        print("wombat")
    elif command_list[0] == "loadr":
        loadr(command_list[1])
        #except:
        #	print("ERROR")
    elif command_list[0] == "End":
        bob = 1
        com = -1
        vardict.clear()

    elif command_list[0] == "var":
        vardict[command_list[1]] = command_list[2]
        print( vardict[command_list[1]])


    else:
        print("Error in line: "+str(com+1)+":")
        print("\tcommand "+str(command_list[:]))
        bob = 1
        com = -1
        vardict.clear()
    #elif command_list[0] in loaded:
    #	save_text("text.temp")
    #	args = " ".join(command_list[1:])
    #	os.system(".\\" + command_list[0] + ".py " + args)
    #	open("text.temp")
    #	os.remove("text.temp")
def sp():
    global command
    global pgrm
    command = pgrm.split(";")

def main():
    global bob
    global com
    global command
    global filename
    open_text(filename)
    os.system("cls")

    #if len(sys.argv) > 1:
        #filename = sys.argv[1]

    global text
    #try: open_text(filename)
    #except: print("Default file not found\n\t\"file.txt\" is missing")
    #bob = 1
    while 1:
        if bob == 1:
            interperit(input(">>>"))
            #if autosave: save_text()
        else:
            sp()
            interperit(command[com])
            com+=1


main()
