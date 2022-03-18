import menus
import surveyingcalculus as calc

    


def main():

    options = ["1. Calculte Whole Circle Bearing", 
               "2. Calculate Coordinates from initial point",
               "3. Calculate bearing from WCB",
               "Exit"]
    Title = "Surveying and Levelling"
    option = len(options)
    while option != len(options)-1 and option != None:
        option = menus.list_menu(Title, options)
        if option == 0:
            print("Input initial coordinates")
            initialcoordinates = calc.coordinates_input()
            print("Input final coordinates")
            finalcoordinates = calc.coordinates_input()
            wcb = calc.wcbfromcoordinates(initialcoordinates, finalcoordinates)
            if wcb != None:
                print("the whole circle bearing from coordinates {} to coordinates {} is equal to {}°"
                    .format(initialcoordinates,finalcoordinates,wcb))
        elif option == 1:
           print("-----Input initial coordinates------")
           initialcoordinates = calc.coordinates_input() 
           print("-----Input distance------")
           distance = calc.distance_input()
           print("------Input Whole Circle Bearing-------")
           wcb = calc.wcb_input()
           coordinate = calc.coordinatesfrompoint(initialcoordinates, distance, wcb)
           print("The coordinates for final point are {}".format(coordinate))
        elif option == 2:
            print("------Input Whole Circle Bearing-------")
            wcb = calc.wcb_input()
            print("The bearing is {}".format(calc.formatwcbtobearing(wcb)))
        elif option == len(options)-1:
            print("You are out...")


    return

if __name__ == "__main__":
    main()
