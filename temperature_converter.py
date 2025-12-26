# temperature converter program

#----------------------Celsius to Fahrenheit Conversion----

print("\n----Celsius to Fahrenheit Converter----")
celsius_str = input("Enter temperature in Celsius:  ")
celsius = float(celsius_str)
fahrenheit = (celsius * 9/5) + 32
print(f"Fahrenheit : {fahrenheit} F") # Using an f- string for clearer output


#---------------------Fahrenheit to Celsius Convertion----

print(("\n----Fahrenheit to Celsius Converter---")
farenheit_str = input("Enter temperature in Fahrenheit:  ")
farenheit = float (farenhet_str)
celsius = (farenheit -32) * 5/9
print(f"Celsius : {celsius} C")  # Using an f- string for clearer output
