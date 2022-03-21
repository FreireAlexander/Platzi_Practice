import menus
import subapp as app

def main():

    Title = "Simples Calculations"
    options = ["1. Calculte Coordinates", 
               "2. Calculate Whole Circle Bearing",
               "3. Calculate Bearing",
               "4. Convert decimals angles to DDMMSS and Viceversa",
               "Exit"]

    option = len(options)
    
    while option != len(options)-1 and option != None:
        option = menus.list_menu(Title, options)
        # Application 1 Calculate Coordinates is ok
        if option == 0:
            app.simplecalculatecoordinates()
        elif option == 1:
            app.simplecalculatewcb()
        elif option == 2:
            app.simplecalculaterb()
        elif option == 3:
            app.simpleangleconvertion()
        elif option == len(options)-1:
            print("You are out...")

    return

if __name__ == "__main__":
    main()
