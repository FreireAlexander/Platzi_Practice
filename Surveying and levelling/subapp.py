import menus
import calculus as calc
import validation as val
import typeindata as load

def simplecalculatecoordinates():
    
    point_order = "initial point to final point"
    subtitle = "Which coordinates do you know?"
    suboptions = [
        "1. Initial Point coordinates",
        "2. Final Point coordinates"
    ]
    coordinate_choice = menus.list_menu(subtitle, suboptions)

    coordinates = []
    coordinates = load.Coordinates()

    subtitle = "Which angle do you know?"
    suboptions = [
            "1. Whole Circle Bearing",
             "2. Reduced Bearing",
            "3. Back Bearing"
            ]
    angle_choice = menus.list_menu(subtitle, suboptions)

         # from angle calculate wcb
    wcb = 0
    if angle_choice == 0 or angle_choice == None:
        print("------Input Whole Circle Bearing------")
        print("** Angles must be introduces as positive")
        wcb = load.angle()

    elif angle_choice == 1:
        print("------Input Reduced Bearing------")
        print("** Angles must be introduces as positive")
        wcb = load.angle()  # This must be different

    elif angle_choice == 2:
        print("------Input Back Bearing------")
        print("** Angles must be introduces as positive")
        wcb = load.angle()
        wcb = calc.backbearing(wcb)

    print("------Input distance-----------------")
    distance = 0
    distance = load.distance()

    if coordinate_choice == 1:
        point_order = "final point to initial point"

    coord_result = calc.coordinatesfrompoint(coordinates, distance, wcb)
    menus.clear()
    print("\tThe coordinates from {} are equals to {} ".format(
    point_order, coord_result))
    print("\twhere whole circle bearing would be {}° ".format(round(wcb, 3)))
    print("\tand distance from {} {} to {} is {} m ".format(point_order,
                                                coordinates, coord_result, distance))
    print("\nPress Enter to continue...")
    input()
    menus.clear()

    return

def simplecalculatewcb():

    subtitle = "What information do you have?"
    suboptions = [
        "1. WCB between two coordinates",
        "2. A Reduced Bearing",
        "3. A Back Whole circle Bearing"
    ]

    info_choice = menus.list_menu(subtitle, suboptions)

    if info_choice == 0:
        print("\t Input initial point Coordinates")
        initialcoordinates = []
        initialcoordinates = load.Coordinates()
        menus.clear()
        print("\t Input final point Coordinates")
        finalcoordinates = []
        finalcoordinates = load.Coordinates()
        wcb = calc.wcbfromcoordinates(initialcoordinates, finalcoordinates)
        menus.clear()
        print("\n\tWCB from point {} to {} is equals to {}".format(initialcoordinates,finalcoordinates,wcb))
    elif info_choice == 1:
        print("Esto es lo que puedo hacer por ahora sin el RD")
    elif info_choice == 2:
        print("------Input Back Bearing------")
        print("** Angles must be introduces as positive")
        wcb = load.angle()
        backbearing = wcb
        wcb = calc.backbearing(wcb)
        menus.clear()
        print("the Whole Circle Bearing from backbearing of {} is equal to {}".format(backbearing,wcb))

    print("\nPress Enter to continue...")
    input()
    menus.clear()

    return


def simplecalculaterb():
    print("I'm doing nothing yet...")
    return

def simpleangleconvertion():
    subtitle = "What do you want to do?"
    suboptions = [
        "1. Convert Degree Minutes Seconds to Decimals",
        "2. Convert Decimals to Degree Minutes Seconds"
    ]
    choice = menus.list_menu(subtitle, suboptions)
    if choice == 0:
        print("------Input Angle------")
        angle = load.angledms()
        angle_input = angle
        angle = val.bearingdata(angle)
        degree = 0
        if angle[3] == "":
            degree = float(angle[0]) + float(angle[1])/60 + float(angle[2])/3600
        else:
            degree = float(angle[0]) + float(angle[1])/60 + float(angle[2])/3600
            degree = str(degree) +" in quadrant "+ angle[3]
        print("The angle {} is equal to {}°".format(angle_input,degree))
    elif choice == 1:
        print("------Input Angle------")
        print("** Angles must be introduces as positive")
        angle = load.angle()
        angledms = calc.decimaltodms(angle)
        print("the angle {}° is equal to {}".format(angle,angledms))

    print("\nPress Enter to continue...")
    input()
    menus.clear()

    return