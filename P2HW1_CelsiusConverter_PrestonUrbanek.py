#This program converts Celsius to Fahrenheit
#9/22/2018
#CTI 110 P2HW1
#Preston Urbanek

celsiusTemp = float( input('Please enter a temperature in celsius: '))

fahrenheitTemp = ( ( 9/5 ) * celsiusTemp) + 32

print(str(celsiusTemp) + ' in celsius converted to fahrenheit is: ' + str(fahrenheitTemp))
