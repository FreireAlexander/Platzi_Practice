def cursor_UP_DOWN(option):
    import readchar
    import os
    
    key_arrow = readchar.readkey()

    if key_arrow == "\x1b\x5b\x41":
        option -= 1
    elif key_arrow == "\x1b\x5b\x42":
        option += 1
    return option, key_arrow
    

def menu(Title,*args):

    import readchar
    import os

    # arrow image in ASCII
    arrow = "-->"

    isValid = True

    option = 0

    while isValid:

        # Drawing menu
        print("---------- {} -----------".format(Title))
        for a in args:
            if args.index(a) == option:
                print("{}\t{}".format(arrow,a))
            else:
                print("\t{}".format(a))
        
        # Catching cursor

        option,key_arrow = cursor_UP_DOWN(option)
        os.system("cls")
        
        #Validating option
        if option <= -1:
            option = len(args)-1
        elif option > len(args)-1:
            option = 0

        #Enter to exit

        if key_arrow == "\x0d":
            isValid = False
            

    return option+1



def main():
    
    option = menu("Menu", "Golpe Certero", "Ataque ninja", "Postres", "Empanadas","Salir")
    print(option)


if __name__ == "__main__":
    main()
    




    
    








