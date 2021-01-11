Ta= int(input("Enter the temperature in Fahrenheit: "))

V= int(input("Now, enter the wind speed in mph: "))

Twc= (34.74+(0.6215*Ta)-((35.75)*(V**0.16))+(0.4275*(V**0.16)))

print("Windchill= "+ str(Twc))
