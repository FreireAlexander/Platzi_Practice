import readchar
import os

'''
UP = "\x1b\x5b\x41"
DOWN = "\x1b\x5b\x42"
LEFT = "\x1b\x5b\x44"
RIGHT = "\x1b\x5b\x43"
'''

def cursor_UP_DOWN(option):
    
    key_arrow = readchar.readkey()

    if key_arrow == "\x1b\x5b\x41":
        option -= 1
    elif key_arrow == "\x1b\x5b\x42":
        option += 1
    return option, key_arrow 

def menu_vertical(Title,args):

    # arrow image in ASCII
    arrow = "-->"

    isValid = True

    if len(args) < 1:
        isValid = False
        return "Options must be greater than 1"

    option = 0

    while isValid:

        # Drawing menu
        print("---------- {} -----------".format(Title))
        for a in args:
            if args.index(a) == option:
                print("{}\t{}".format(arrow,a))
            else:
                print("\t{}".format(a))
            #Esc to exit menu or press Enter to select option   
        print("\nEsc to exit or press Enter to select option\n")
        # Catching cursor

        option,key_arrow = cursor_UP_DOWN(option)
        os.system("cls")
        
        #Validating option
        if option <= -1:
            option = len(args)-1
        elif option > len(args)-1:
            option = 0

        #Enter to select option
        if key_arrow == "\x0d":
            isValid = False
            return option + 1

        #Esc to exit menu and return None, None options selected
        if key_arrow == "\x1b":
            isValid = False
            return None


def cursor_UDLR(option,col):
    
    key_arrow = readchar.readkey()
    if key_arrow == "\x1b\x5b\x41": #UP
        option -= col
    elif key_arrow == "\x1b\x5b\x42": #DOWN
        option += col
    elif key_arrow == "\x1b\x5b\x43": #RIGHT
        option += 1
    elif key_arrow == "\x1b\x5b\x44": #LEFT
        option -= 1
    return option, key_arrow  


def menu_horizontal(col, Title,args):

    # arrow image in ASCII
    arrow = "-->"
    
    isValid = True

    if len(args) < 1:
        isValid = False
        return "Options must be greater than 1"

    option = 0

    while isValid:

        # Drawing menu
        print("---------- {} -----------".format(Title))

        for a in args:
            if args.index(a)%col == 0 and args.index(a) != 0:
                print("\n")


            if args.index(a) == option:
                print(" {} {}".format(arrow,a),end="")
            else:
                print("   {} ".format(a), end="")
            
            #Esc to exit menu or press Enter to select option
            

        print("\n\nEsc to exit or press Enter to select option\n")
        
        # Catching cursor

        option,key_arrow = cursor_UDLR(option,col)
        os.system("cls")
        
        #Validating option
        if option <= -1:
            option = len(args)-1
        elif option > len(args)-1:
            option = 0

        #Enter to select option
        if key_arrow == "\x0d":
            isValid = False
            return option + 1

        #Esc to exit menu and return None, None options selected
        if key_arrow == "\x1b":
            isValid = False
            return None


def main():
    Title = "Menu"
    options = ["Sushi", "Tacos", "Hot Dogs", "Lasagna", "Guandul","Mote", "Queso", "Perro", "Gato"]
    # option = menu_horizontal(3,Title,options)
    option = menu_vertical(Title, options)
    print(option)


if __name__ == "__main__":
    main()
    




    
    








