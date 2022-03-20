import re

def positive_number_validation(number):
	num_format = re.compile(r'^[0-9]*[.0-9]*$')
	return re.match(num_format,number)

def number_validation(number):
	num_format = re.compile(r'^\-?[0-9]*[.0-9]*$')
	return re.match(num_format,number)

def coordinates_input():
	coordinates = [0,0]
	it_is = False

	while not it_is:
		coordinates[0] = input("Input Coordinate X: ")
		num_format = re.compile(r'^\-?[0-9]*.[0-9]*$')
		it_is = re.match(num_format,coordinates[0])

	coordinates[0] = float(coordinates[0])

	it_is = False

	while not it_is:
		coordinates[1] = input("Input Coordinate Y: ")
		num_format = re.compile(r'^\-?[0-9]*.[0-9]*$')
		it_is = re.match(num_format,coordinates[1])

	coordinates[1] = float(coordinates[1])

	return coordinates


def main():
    print("-----Input distance-----------------")
    distance = input("Input distance from initial point: ")
    while not number_validation(distance):
        print("Remenber wcb must a number")
        distance = input("Input Whole Circle Bearing: ")

    return

if __name__ == "__main__":
    main()
