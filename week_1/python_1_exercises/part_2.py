# user_input = int(input("Enter a number:  "))

# if(user_input % 2 == 0):
#     print("The number you enter is even number")
# elif(user_input % 4 == 0):
#     print("The number you enter is a multiple of four")
# else:
#     print("The number you enter is odd")
# print("*******************************************************")

# user_input_four = int(input("Enter a number: "))

# if(user_input_four % 4 == 0):
#     print("The number you just enter is a mulptiple of 4")
# else:
#     print("The number you just enter is not a mulptiple of 4")
# print("*******************************************************")

# fizz_buzz_number = int(input("Type a number: "))

# if(fizz_buzz_number % 3 == 0):
#     print('fizz')
# elif(fizz_buzz_number % 5 == 0):
#     print("buzz")
# else:
#     print("Your number is not either fizz or buzz!!!")


#Converting temperature
temperature_unit = input('Type the unit of the temperature either c or f:  ')
temperature_unit = temperature_unit.lower()
temperature_number = int(input('Type the temperature number:  '))

calculate_temp_celcius = ((temperature_number - 32) * (5/9))
calculate_temp_fahrenheit = ((temperature_number * 1.8) + 32)

if(temperature_unit == 'c'):
    print(f'You enter {temperature_number} degree celcius this is {calculate_temp_fahrenheit}f in fahrenheit')
elif(temperature_unit == 'f'):
    print(f'You enter {temperature_number} degree fahrenheit this is {calculate_temp_celcius}c in celsius')
else:
    print("I think you typed the wrong letters, please, type only the letter F or C, and a number")