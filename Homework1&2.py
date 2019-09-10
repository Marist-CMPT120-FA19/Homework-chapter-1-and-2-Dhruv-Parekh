#Dhruv Parekh CMPT Homework Chapter 1 & 2

#1
print("Hello, World")
print("Hello", "World")
print(3)
print(3.0)
print(2+3)
print(2.0+3.0)
print("2"+"3")
print("2+ 3=", 2+ 3)
print(2**3)
print(2*3)
print(7/3)
print(7//3)
#2

def main():
    print("This program illustrates a chaotic function")
    x = input("Enter a number between 0 and 1: ")
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)
main()

#3
def main():
    print("This program illustratessss a chaotic function")
    x = input("Enter a number between 0 and 1: ")
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)
main()

##The difference between these two programs is the formula. The orignal function multiplies the number in such a way that they get smaller. The other function multipies the number by 1 giving you the same number at every level of the loop.

#4
def main():
    print("This program illustrates a chaotic function")
    x = input("Enter a number between 0 and 1: ")
    for i in range(20):
        x = 3.9 * x * (1 - x)
        print(x)
main()


#5
def main():
    print("This program illustrates a chaotic function")
    x = input("Enter a number between 0 and 1: ")
    n = (input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)
main()



#Chapter 2

#1
def main():
    print("This program converts Celsius temperatures to Farenheit")
    celsius = (input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()


#4
def main():
    print("This program converts Celsius temperatures to Farenheit")
    for i in range(5):
        celsius = (input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()

#6
def main():
    print("This program calculates the future value")
    print("of an investment period.")

    principal = (input("Enter the initial principal: "))
    apr = (input("Enter the annual interest rate: "))
    time = (input("Number of years"))

    for i in range(time):
        principal = principal * (1 + apr)

    print(principal, "is the amount in", time, "years")

main()