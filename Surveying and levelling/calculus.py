import math
import re

# Coordinates configuration [East or X, North or Y]

def is_wcb_360(wcb):
	while wcb >= 360:
		wcb = wcb - 360
	return wcb


def backbearing(wcb):
	wcb = is_wcb_360(wcb)
	if wcb <= 180:
		return wcb + 180
	elif wcb > 180:
		return wcb - 180
	

def wcbtoreducedbearing(wcb):
	wcb = is_wcb_360(wcb)
	rb = wcb
	if wcb == 0:
		rb = 0
	elif wcb > 0 and wcb < 90:
		rb = wcb 
	elif wcb == 90:
		rb = 90
	elif wcb > 90 and wcb < 180:
		rb = 180 - wcb 
	elif wcb == 180:
		rb = 180
	elif wcb > 180 and wcb < 270:
		rb = wcb - 180 
	elif wcb == 270:
		rb = 270
	elif wcb > 270 and wcb < 360:
		rb = 360 - wcb 
	elif wcb == 360:
		rb = 0

	return rb


def decimaltodms(angle):
	dms = ""
	degree = int(angle)
	dms += str(degree) + "°"
	minutes = int((angle - degree)*60)
	dms += str(minutes) + "°"
	seconds = round(float(((angle - degree)*60 - minutes)*60),3)
	dms += str(seconds) + "°"
	return dms

def format_wcbtorb(wcb):
	wcb = is_wcb_360(wcb)
	rb = wcb
	if wcb == 0:
		rb = 0
		return "N " + decimaltodms(rb) + " E"
	elif wcb > 0 and wcb < 90:
		rb = wcb 
		return "N " + decimaltodms(rb) + " E"
	elif wcb == 90:
		rb = 90
		return "S " + decimaltodms(rb) + " E"
	elif wcb > 90 and wcb < 180:
		rb = 180 - wcb
		return "S " + decimaltodms(rb) + " E" 
	elif wcb == 180:
		rb = 180
		return "S " + decimaltodms(rb) + " E"
	elif wcb > 180 and wcb < 270:
		rb = wcb - 180 
		return "S " + decimaltodms(rb) + " W"
	elif wcb == 270:
		rb = 270
		return "S " + decimaltodms(rb) + " W"
	elif wcb > 270 and wcb < 360:
		rb = 360 - wcb 
		return "N " + decimaltodms(rb) + " W"
	elif wcb == 360:
		rb = 0
		return "N " + decimaltodms(rb) + " W"


def angle(latitude, departure):
	return math.degrees(math.atan(departure/latitude))



def wcbfromcoordinates(initialcoordinates, finalcoordinates):
	wcb = 0 # This is the whole circle bearing // Azimut en español
	latitude = finalcoordinates[1] - initialcoordinates[1]
	departure = finalcoordinates[0] - initialcoordinates[0]
	if latitude == 0 and departure == 0:
		return "0 you have entered the same coordinates..."
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
		return "You have entered the same coordinates..."


def coordinatesfrompoint(initialcoordinates,distance,wcb):
	coordinates = [0,0]
	coordinates[0] = round(initialcoordinates[0] + distance*math.sin(math.radians(wcb)),3)
	coordinates[1] = round(initialcoordinates[1] + distance*math.cos(math.radians(wcb)),3)

	return coordinates