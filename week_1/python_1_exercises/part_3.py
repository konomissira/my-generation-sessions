age = int(input("Please, enter your age: "))
salary = int(input("Please, enter your salary: "))

if(21 <= age < 30 and 21000 <= salary < 35000):
    print("You can loan £50,000")
elif(age >=30 and 35000 <= salary < 50000):
    print("You can loan £75,000")
elif(age >= 30 and 50000 <= salary < 100000):
    print("You can loan £100,000")
else:
    print("You are not eligible for a loan!")