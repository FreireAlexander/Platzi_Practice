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

    subtitle = "How do you prefer to insert angles?"
    suboptions = [
            "1. decimal angle ",
            "2. in DD°MM'SS'' "
            ]
    angle_format = menus.list_menu(subtitle, suboptions)
         # from angle calculate wcb
    
    if angle_format != 1:
        
        if angle_choice == 0 or angle_choice == None:
            print("------Input Whole Circle Bearing------")
            print("** Angles must be introduces as positive")
            wcb = load.angle()
            wcbangle = wcb

        elif angle_choice == 1:
            print("------Input Reduced Bearing------")
            print("** Angles must be introduces as positive")
            wcb = load.rbdecimal()
            angle = wcb
            angle = val.bearingdata_decimal(angle)
            angle = calc.rbdecimaltowcb(angle)
            wcbangle = angle

        elif angle_choice == 2:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            wcb = load.angle()
            wcb = calc.backbearing(wcb)
            wcbangle = wcb

    elif angle_format == 1:
        
        if angle_choice == 0 or angle_choice == None:
            print("------Input Whole Circle Bearing------")
            print("** Angles must be introduces as positive")
            wcb = load.dms()
            angle = wcb
            angle = val.bearingdata(angle)
            angle = calc.dmstodecimals(angle)
            wcbangle = angle

        elif angle_choice == 1:
            print("------Input Reduced Bearing------")
            print("** Angles must be introduces as positive")
            wcb = load.reducedbearing()
            angle = wcb
            angle = val.bearingdata(angle)
            angle = calc.rbdmstowcb(angle)
            wcbangle = angle

        elif angle_choice == 2:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            wcb = load.dms()
            angle = wcb 
            angle = val.bearingdata(angle)
            angle = calc.dmstodecimals(angle)
            angle = calc.backbearing(angle)
            wcbangle = angle

        
    print("------Input distance-----------------")
    distance = 0
    distance = load.distance()

    if coordinate_choice == 1:
        point_order = "final point to initial point"

    coord_result = calc.coordinatesfrompoint(coordinates, distance, wcbangle)
    menus.clear()
    print("\tThe coordinates from {} are equals to {} ".format(
    point_order, coord_result))
    print("\twhere whole circle bearing would be {} ".format(calc.decimaltodms(wcbangle)))
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
        print("\n\tWCB from point {} to {} is equals to {}".format(initialcoordinates,finalcoordinates,calc.decimaltodms(wcb)))
    elif info_choice == 1:
        subtitle = "How do you prefer to insert angles?"
        suboptions = [
            "1. decimal angle ",
            "2. in DD°MM'SS'' "
            ]
        angle_format = menus.list_menu(subtitle, suboptions)
        if angle_format != 1:
            print("------Input Reduced Bearing------")
            print("** Angles must be introduces as positive")
            wcb = load.rbdecimal()
            rb = wcb
            angle = wcb
            angle = val.bearingdata_decimal(angle)
            angle = calc.rbdecimaltowcb(angle)
            wcbangle = angle
            print("\tthe Whole Circle Bearing from reduced bearing of {} is equal to {}".format(rb,wcbangle))
        elif angle_format == 1:
            print("------Input Reduced Bearing------")
            print("** Angles must be introduces as positive")
            wcb = load.reducedbearing()
            rb = wcb
            angle = wcb
            angle = val.bearingdata(angle)
            angle = calc.rbdmstowcb(angle)
            wcbangle = angle
            print("\tthe Whole Circle Bearing from reduced bearing of {} is equal to {}".format(rb,calc.decimaltodms(wcbangle)))
    
    elif info_choice == 2:
        subtitle = "How do you prefer to insert angles?"
        suboptions = [
            "1. decimal angle ",
            "2. in DD°MM'SS'' "
            ]
        angle_format = menus.list_menu(subtitle, suboptions)
        if angle_format != 1:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            wcb = load.angle()
            backbearing = wcb
            wcb = calc.backbearing(wcb)
            menus.clear()
            print("\tthe Whole Circle Bearing from backbearing of {} is equal to {}".format(backbearing,wcb))
        elif angle_format == 1:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            wcb = load.dms()
            backbearing = wcb
            angle = wcb 
            angle = val.bearingdata(angle)
            angle = calc.dmstodecimals(angle)
            angle = calc.backbearing(angle)
            wcbangle = calc.decimaltodms(angle)
            print("\tthe Whole Circle Bearing from backbearing of {} is equal to {}".format(backbearing,wcbangle))
    print("\nPress Enter to continue...")
    input()
    menus.clear()

    return


def simplecalculaterb():
    subtitle = "What information do you have?"
    suboptions = [
        "1. Reduced Bearing between two coordinates",
        "2. A Whole Circle Bearing",
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
        rb = calc.format_wcbtorb(wcb)
        menus.clear()
        print("\n\tReduced Bearing from point {} to {} is equals to {}".format(initialcoordinates,finalcoordinates,rb))
    elif info_choice == 1:
        subtitle = "How do you prefer to insert angles?"
        suboptions = [
            "1. decimal angle ",
            "2. in DD°MM'SS'' "
            ]
        angle_format = menus.list_menu(subtitle, suboptions)
        if angle_format != 1:
            print("------Input Whole Circle Bearing------")
            print("** Angles must be introduces as positive")
            wcb = load.angle()
            rb = calc.wcbdecimaltorbdecimal(wcb)
            wcb = round(wcb,3)
            print("\tthe Reduced Bearing from WCB of {}° is equal to {}".format(wcb,rb))
        elif angle_format == 1:
            print("------Input Wcb------")
            print("** Angles must be introduces as positive")
            wcb = load.dms()
            rb = wcb
            rb = val.bearingdata(rb)
            rb = calc.dmstodecimals(rb)
            rb = calc.format_wcbtorb(rb)
            print("\tthe Reduced Bearing from wcb of {} is equal to {}".format(wcb,rb))
    
    elif info_choice == 2:
        subtitle = "How do you prefer to insert angles?"
        suboptions = [
            "1. decimal angle ",
            "2. in DD°MM'SS'' "
            ]
        angle_format = menus.list_menu(subtitle, suboptions)
        if angle_format != 1:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            wcb = load.angle()
            backbearing = wcb
            wcb = calc.backbearing(wcb)
            rb = calc.wcbdecimaltorbdecimal(wcb)
            menus.clear()
            print("\tthe Reduced Bearing from  Back Bearing of {} is equal to {}".format(backbearing,rb))
        elif angle_format == 1:
            print("------Input Back Bearing------")
            print("** Angles must be introduces as positive")
            wcb = load.dms()
            backbearing = wcb
            angle = wcb 
            angle = val.bearingdata(angle)
            angle = calc.dmstodecimals(angle)
            wcb = calc.backbearing(angle)
            rb = calc.format_wcbtorb(wcb)
            print("\tthe Reduced Bearing from  Back Bearing of {} is equal to {}".format(backbearing,rb))
    
    print("\nPress Enter to continue...")
    input()
    menus.clear()

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
        if angle[3] == '':
            degree = round(calc.dmstodecimals(angle),3)
            degree = str(degree) +"°"
        else:
            degree = round(calc.dmstodecimals(angle),3)
            degree = str(degree) +"° in quadrant "+ angle[3]
        print("The angle {} is equal to {}".format(angle_input,degree))
    elif choice == 1:
        print("------Input Angle------")
        print("** Angles must be introduces as positive")
        angle = load.angle()
        angle = round(angle, 3)
        angledms = calc.decimaltodms(angle)
        print("the angle {}° in range [0 to 360°] is equal to {}".format(angle,angledms))

    print("\nPress Enter to continue...")
    input()
    menus.clear()

    return