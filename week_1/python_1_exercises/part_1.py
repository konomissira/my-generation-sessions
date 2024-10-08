#Create a variable to store the first name
first_name = "Mahamadou"
print(first_name)
print("********************************************")

#Create a variable to store the lastname
last_name = "Camara"

#Concatenate the two variables
full_name = first_name + last_name
print(f"Hello {full_name}")
print("********************************************")

greeting = f"My name is {first_name} {last_name}"
print(greeting)
print("********************************************")

#First Value
first_value = 15

#Second Value
second_value = 8

product = first_value * second_value
print(product)
print("********************************************")

presenting_value = f"The product of {first_value} and {second_value} is {product}"
print(presenting_value)
print("********************************************")

people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

third_element = people[2]
print(third_element)
print("********************************************")

third_element_from_back = people[-3]
print(third_element_from_back)
print("********************************************")

new_list = people[2:6]
print(new_list)
print("********************************************")

compare_first_and_last_element = people[0] == people[-1]
print(compare_first_and_last_element)
print("********************************************")

name = input("What is your name? ")
print(f"Welcome {name}")
print("********************************************")

first_number = int(input("Enter a number a first number " ))
second_number = int(input("Enter a number a second number " ))

multiplication = first_number * second_number
print(multiplication)
print("********************************************")

number_one = int(input("Type your first number "))
number_two = int(input("Type your second number "))

compare_two_numbers = number_one == number_two
print(compare_two_numbers)