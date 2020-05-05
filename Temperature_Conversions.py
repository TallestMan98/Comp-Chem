#Temperature Calculator

Farenheit = input ("The temperature in Farenheit is ")

Farenheit_Float = float(Farenheit)

Celcius = (5*(Farenheit_Float - 32))/9

print("The temperature in Celcius is {:.2f}".format(Celcius))

Kelvin = Celcius + 273.15

print("The temperature in Kelvin is {:.2f}".format (Kelvin))