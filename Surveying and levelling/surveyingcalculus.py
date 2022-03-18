import math
import re

# Coordinates configuration [East or X, North or Y]

def wcb_input():
	it_is = False
	while not it_is:
		wcb = input("Input Whole Circle Bearing: ")
		num_format = re.compile(r'^[0-9]*.[0-9]*$')
		it_is = re.match(num_format,wcb)

	wcb = float(wcb)
	while wcb >= 360:
		wcb -= 360
		
	return wcb

def distance_input():
	it_is = False
	while not it_is:
		distance = input("Input distance: ")
		num_format = re.compile(r'^[0-9]*.[0-9]*$')
		it_is = re.match(num_format,distance)

	distance = float(distance)
	return distance

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

def wcbtobearing(wcb):
	bearing = wcb
	if wcb == 0:
		bearing = 0
	elif wcb > 0 and wcb < 90:
		bearing = wcb 
	elif wcb == 90:
		bearing = 90
	elif wcb > 90 and wcb < 180:
		bearing = 180 - wcb 
	elif wcb == 180:
		bearing = 180
	elif wcb > 180 and wcb < 270:
		bearing = wcb - 180 
	elif wcb == 270:
		bearing = 270
	elif wcb > 270 and wcb < 360:
		bearing = 360 - wcb 
	elif wcb == 360:
		bearing = 0
	
	return bearing

def formatwcbtobearing(wcb):
	bearing = wcb
	if wcb == 0:
		bearing = 0
		return "N " + str(bearing)
	elif wcb > 0 and wcb < 90:
		bearing = wcb 
		return "N " + str(bearing) + " E"
	elif wcb == 90:
		bearing = 90
		return "E " + str(bearing)
	elif wcb > 90 and wcb < 180:
		bearing = 180 - wcb
		return "S " + str(bearing) + " E" 
	elif wcb == 180:
		bearing = 180
		return "S " + str(bearing)
	elif wcb > 180 and wcb < 270:
		bearing = wcb - 180 
		return "S " + str(bearing) + " W"
	elif wcb == 270:
		bearing = 270
		return "W " + str(bearing)
	elif wcb > 270 and wcb < 360:
		bearing = 360 - wcb 
		return "N " + str(bearing) + " W"
	elif wcb == 360:
		bearing = 0
		return "N " + str(bearing)


def angle(latitude, departure):
	return math.degrees(math.atan(departure/latitude))


def wcbfromcoordinates(initialcoordinates, finalcoordinates):

	wcb = 0 # This is the whole circle bearing // Azimut en español

	latitude = finalcoordinates[1] - initialcoordinates[1]
	departure = finalcoordinates[0] - initialcoordinates[0]

	if latitude == 0 and departure == 0:
		wcb = "Error, las coordenadas son iguales"
	elif latitude >= 0 and departure >= 0:
		if latitude == 0: # Para evitar la divisón entre cero para calcular el azimut cuando la proyección Norte es de cero
			wcb = 90
		else:
			wcb = angle(latitude,departure) # Primer cuadrante o arriba a la derecha
	elif latitude <= 0 and departure >= 0:
			wcb = 180 + angle(latitude,departure) # Segundo cuadrante o abajo a la derecha
	elif latitude <= 0 and departure <= 0:
		if latitude == 0: # Para evitar la divisón entre cero para calcular el azimut cuando la proyección Norte es de cero
			wcb = 270
		else:
			wcb = 180 + angle(latitude,departure) # Tercer Cuadrante o abajo a la izquierda
	elif latitude >= 0 and departure <= 0:
		wcb = 360 + angle(latitude,departure) # Cuarto cuadrante o arriba a la izquierda
	try:
		return round(wcb,3)	
	except TypeError:
		print("You have entered the same coordinates...")


def coordinatesfrompoint(initialcoordinates,distance,wcb):
	coordinates = [0,0]
	coordinates[0] = round(initialcoordinates[0] + distance*math.sin(wcb),3)
	coordinates[1] = round(initialcoordinates[1] + distance*math.cos(wcb),3)
	return coordinates
