#by petrucciii

#import module
import calculator

calc_again = "yes"

#title
print("Calculator")

try:

    while calc_again == "yes" or calc_again == "Yes":
        
        #option
        print("\nSelect operation")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

        #enter the choice
        choice = int(input("\nEnter choice (1/2/3/4): "))

        #choose the numbers
        num1 = int(input("\nChoose the first number: "))
        num2 = int(input("Choose the second number: "))

        #making the operation
        if choice == 1:
            add = calculator.add(num1,num2)
            print(add)
        elif choice == 2:
            subtract = calculator.subtract(num1,num2)
            print(subtract)
        elif choice == 3:
            multiply = calculator.multiply(num1,num2)
            print(multiply)
        elif choice == 4:
            divide = calculator.divide(num1,num2)
            print(divide)

        #make another operation
        calc_again = input("Do you want to make another calculation? ")

#string error
except:

    print("TYPE A NUMBER!")

    try:

        while calc_again == "yes" or calc_again == "Yes":

            print("\nSelect operation")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")

            choice = int(input("\nEnter choice (1/2/3/4): "))

            num1 = int(input("\nChoose the first number: "))
            num2 = int(input("Choose the second number: "))


            if choice == 1:
                add = calculator.add(num1,num2)
                print(add)
            elif choice == 2:
                subtract = calculator.subtract(num1,num2)
                print(subtract)
            elif choice == 3:
                multiply = calculator.multiply(num1,num2)
                print(multiply)
            elif choice == 4:
                divide = calculator.divide(num1,num2)
                print(divide)

            calc_again = input("Do you want to make another calculation? ")

    except:

        print("TYPE A NUMBER!")

#exit
input("Press Enter to Exit")