fileboi = "/users/alexandermoening/whirlcode/file.txt"


def main(filename):
    file = open(filename, "r")
    filestring = file.read()
    linelist = filestring.split("\n")

    lbls = {}
    lbllinecount = 0
    for i in linelist:

        i2 = i.split(",")
        if i2[0] == "lbl" or i2[0] == "label":
            lbls[i2[1]] = lbllinecount
        lbllinecount = lbllinecount + 1

    strvars = {}

    def get_str_var(name):
        return strvars[name]

    def add_str_var(name, data):
        strvars[name] = data
    run = True
    count = 0

    while run == True:
        goto = False

        line = linelist[count]
        command = line.split(",")

        if command[0] == "math":
            if command[1] == "add var to var":
                addsum = int(get_str_var(command[2])) + int(get_str_var(command[3]))
                add_str_var(str(command[4]), addsum)

        elif command[0] == "IO":
            # Input/Output functions here
            if command[1] == "out":
                if command[2] == "str":
                    print(command[3])
                elif command[2] == "var":
                    print(get_str_var(command[3]))
            elif command[1] == "in":
                strvars[command[2]] = input(command[3])

        elif command[0] == "var":
            if command[1] == "str":
                add_str_var(command[2], command[3])

        elif command[0] == "goto":
            goto = True
            if command[1] == "line":
                count = int(command[2])
            if command[1] == "label":
                count = int(lbls[command[2]])

        elif command[0] == "run":
            main(command[1])
        elif command[0] == "if":
            if command[1] == "var to var":
                if get_str_var(command[2]) == get_str_var(command[3]):
                    count = int(lbls[command[4]])
        elif command[0] == "end":
            run = False
        else:
            print("error in line "+str(count) + "")
            print("command "+line+" not found")
            break


        if goto == False or run == False:
            count = count + 1

main(fileboi)