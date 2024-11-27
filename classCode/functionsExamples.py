# name = input("What is your name?") # calling input function
# print("Hi", name) # calling print function


def add_two_numbers(nr1, nr2):
    result = nr1 + nr2
    print(result)
    return result, 6

number_result = add_two_numbers(4, 5)
print(number_result)

def check_patient(temperature, age):
    if temperature > 38 and age > 60:
        print("Fever detected - high risk patient")
    elif temperature > 38:
        print("Fever detected")
    elif temperature > 37 and temperature < 38:
        print("Slight fever.")
    else:
        print("Normal temperature.")


check_patient(39, 33)
check_patient(37, 60)


def greet():
    print("hi")
    print("merhaba")
    print("ola")
    print("bonjour")
    print("marhaban")
    print("ciao")


greet()
