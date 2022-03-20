import menus
import calculus as calc
import validation as val




def main():

    Title = "Simples Calculations"
    options = ["1. Calculte Coordinates", 
               "2. Calculate Whole Circle Bearing",
               "3. Calculate Bearing",
               "Exit"]

    option = len(options)
    
    while option != len(options)-1 and option != None:
        option = menus.list_menu(Title, options)
        if option == 0:
           point_print = "initial point to final point"
           subtitle = "Which coordinates do you know?"
           suboptions = [
               "1. Initial Point coordinates",
               "2. Final Point coordinates"
           ]
           coordinate_choice = menus.list_menu(subtitle, suboptions)
           
           
           coordinates = [0,0]   
           coordinates[0] = input("Input horizontal coordinates: ")
           while not val.number_validation(coordinates[0]):
               print("Remenber coordinates must be a number")
               coordinates[0] = input("Input horizontal coordinates: ")
           
           coordinates[0] = val.ToNumber(coordinates[0])

           coordinates[1] = input("Input vertical coordinates: ")
           while not val.number_validation(coordinates[1]):
               print("Remenber coordinates must be a number")
               coordinates[1] = input("Input horizontal coordinates: ")
           
           coordinates[1] = val.ToNumber(coordinates[1])

           subtitle = "Which angle do you know?"
           suboptions = [
               "1. Whole Circle Bearing",
               "2. Reduced Bearing",
               "3. Back Bearing"
           ]
           angle_choice = menus.list_menu(subtitle, suboptions)
           
           # from angle calculate wcb
           if angle_choice == 0 or angle_choice == None:
               print("------Input Whole Circle Bearing------")
               print("** Angles must be introduces as positive")
               wcb = input("Input WCB: ")
               while not val.positive_number_validation(wcb):
                print("angles must be a number")
                print("** Remenber angles must be introduces as positive")
                wcb = input("Input WCB: ")

               wcb = float(calc.is_wcb_valid(float(wcb)))
               
           elif angle_choice == 1:
               print("------Input Reduced Bearing------")
               print("** Angles must be introduces as positive")
               wcb = input("Input Reduced Bearing: ")
               while not val.positive_number_validation(wcb):
                print("angles must be a number")
                print("** Remenber angles must be introduces as positive")
                wcb = input("Input Reduced Bearing: ")

               wcb = calc.is_wcb_valid(float(wcb))
               wcb = wcb
           elif angle_choice == 2:
               print("------Input Back Bearing------")
               print("** Angles must be introduces as positive")
               wcb = input("Input Back Bearing: ")
               while not val.positive_number_validation(wcb):
                print("angles must be a number")
                print("** Remenber angles must be introduces as positive")
                wcb = input("Input Back Bearing: ")

               wcb = calc.is_wcb_valid(float(wcb))
               wcb = calc.backbearing(wcb)        
           
           

           print("------Input distance-----------------")
           distance = input("Input distance between points: ")
           while not val.positive_number_validation(distance):
               print("Remenber distance must be a number")
               distance = input("Input distance between points: ")
            
           distance = float(distance)

           #Final validation
           if coordinate_choice == 1 and angle_choice == 2:
               wcb = calc.backbearing(wcb)
               point_print = "final point to initial point"

           coordinate = calc.coordinatesfrompoint(coordinates, distance, wcb)
           menus.clear()
           print("The coordinates from {} are equals to {} ".format(point_print,coordinate))
           print("where whole circle bearing would be {}° ".format(round(wcb,3)))
           print("and distance from {} {} to {} is {} m \n".format(point_print,coordinates, coordinate, distance))
           print("Press Enter to continue...")
           input()
           menus.clear()


        elif option == 1:
            '''
            print("Input initial coordinates")
            initialcoordinates = calc.coordinates_input()
            print("Input final coordinates")
            finalcoordinates = calc.coordinates_input()
            wcb = calc.wcbfromcoordinates(initialcoordinates, finalcoordinates)
            if wcb != None:
                print("the whole circle bearing from coordinates {} to coordinates {} is equal to {}°"
                    .format(initialcoordinates,finalcoordinates,round(wcb,3)))
                    '''
        elif option == 2:
            '''
            print("------Input Whole Circle Bearing-------")
            wcb = calc.wcb_input()
            print("The bearing is {}".format(calc.format_wcbtorb(wcb)))
            '''
        elif option == len(options)-1:
            print("You are out...")

    return

if __name__ == "__main__":
    main()
