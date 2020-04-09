print("Welcome to the Temperature Conversion Program\n")
temperatureInFahreneit = float(input("What is the given temperature in degrees Fahrenheit: "))

temperatureInCelcius = round((temperatureInFahreneit - 32)/1.8, 4)
temperatureInKelvin = temperatureInCelcius + 273.15


print('''
Degrees Fahrengeit: \t\t%s
Degrees Celcius:    \t\t%s
Degrees Kelvin:     \t\t%s
''' %(str(temperatureInFahreneit), str(temperatureInCelcius), str(temperatureInKelvin)))
