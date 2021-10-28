# conversion program
# written by Kurtis Norman
# 2nd May 2021

# importing the sleep function to allow timed breaks before code is displayed
import time

# defining all functions and creating a variable for each one
def Kilograms(kg):
    # the return function returns the result. For example, whatever number inputted for 'kg' it is multiplied by 2.2 and returned in a print statement.
    return(kg*2.2)
def Pounds(lb):
    return(lb/2.2)
def Kilometer(km):
    return(km/1.61)
def Mile(m):
    return(m*1.61)
def Celcius(c):
    return((c*1.8)+32)
def Fahrenheit(f):
    return((f-32)/1.8)

# welcomes the user to the program
print("Hello there.\n")
# creating a while loop; the word 'true' means it will loop forever
while True:
    # creates a 1 second gap in the code
    time.sleep(1)
    # creates a variable called choice where the user can choose what they would like to convert
    choice=int(input("What would you like to convert?\n1) Kilograms and Pounds\n2) Kilometers and Miles\n3) Celcius and Farenheit\n answer: "))
    # creating an if loop in response to what the user inputted for the choice variable 
    if choice == 1:
        # creating a variable called 'convert' asking the user if they want to convert from one to another
        convert=int(input("Please pick an option\n1) Kilograms to Pounds\n2) Pounds to Kilograms\n              choice: "))
        # creating an if loop inside an if loop for the user's response to the 'convert' variable
        if convert == 1:
            # using the defined function and variable 'Kilograms' and using float to allow the user to input a decimal if necessary
            kg=Kilograms(float(input("\nEnter how many kilograms you would like to convert: ")))
            # creating a half a second gap in the program before the next bit is displayed
            time.sleep(0.5)
            # creates a gap in the program
            print("\n")
            # displays the return value of the function with the user's input and rounded to 2 decimal places
            print("The amount you entered in kilograms is",round(kg,2), "pounds.\n")
            # another if loop for the other option of the 'convert' variable
            if convert == 2:
                # using the defined function and variable 'Pounds' and using float to allow the user to input a decimal if necessary
                lb=Pounds(float(input("Enter how many pounds you would like to convert: ")))
                # creates a half a second gap in the code before the next bit is displayed
                time.sleep(0.5)
                # creates a gap in the code
                print("\n")
                # displays the return value of the function with the user's input and rounded to 2 decimal places
                print("The amount you entered in pounds is",round(lb,2), "kilograms.\n")
    # creating an else/if statement in response to the choice variable
    elif choice == 2:
        # creating a variable called 'convert2' to allow the user to chosse what they would like to convert from 
        convert2=int(input("\nPlease pick an option\n1) Kilometers to Miles\n2) Miles to Kilometers\n                 choice: "))
        # creating an if loop within an if loop for the user's response to the 'convert2' variable
        if convert2 == 1:
            # using the defined function and variable 'Kilometers' and using float to allow the user to input a decimal if necessary
            km=Kilometer(float(input("\nEnter how many kilometers you would like to convert: ")))
            # creates a half a second gap in the program before displaying the next bit
            time.sleep(0.5)
            # creates a gap
            print("\n")
            # displays the return value of the function with the user's input and rounded to 2 decimal places
            print("The amount you entered in kilometers is",round(km,2), "miles.\n")
        # an if loop for the other option of the 'convert2' variable
        if convert2 == 2:
            # using the defined function and variable 'Mile' and using float to allow the user to input a decimal if necessary
            m=Mile(float(input("\nEnter how many miles you would like to convert: ")))
            # creates a a half a second break in the program before displaying the rest
            time.sleep(0.5)
            # creates a gap in the program
            print("\n")
            # displays the return value of the function with the user's input and rounded to 2 decimal places
            print("The amount you entered in miles is",round(m,2), "kilometers.")
    # ending the the 'choice' if loop    
    else:
        # creating a variable called 'convert3' to allow the user to choose what they would like to convert from
        convert3 = int(input("\nPlease pick an option\n1) Celcius to Fahrenheit\n2) Fahrenheit to Celcius\n                 choice: "))
        # creating an if loop within an if loop for the 'convert3' variable
        if convert3 == 1:
            # using the defined variable and function 'Celcius' and using float to allow the user to enter a decimal if necessary
            c=Celcius(float(input("\nEnter how many degrees celcius would you like to convert: ")))
            # creates a half a second break in the program before displaying the rest 
            time.sleep(0.5)
            # creates a gap in the program
            print("\n")
            # displays the return value of the function with the user's input and rounded to 2 decimal places
            print("The amount you entered in celcius is",round(c,2), "fahrenheit.")
        # an if loop for the other option of the 'convert3' variable
        if convert3 == 2:
            # using the defined function and variable 'Fahrenheit' and using float to allow the user to enter a decimal if necessary   
            f=Fahrenheit(float(input("\nEnter how many degrees fahrenheit would you like to convert: ")))
            # creates a half a second break in the program before displaying the rest
            time.sleep(0.5)
            # creates a gap in the program
            print("\n")
            # displays the return value of the function with the user's input and rounded to 2 decimal places
            print("The amount you entered in fahrenheit is",round(f,2), "celcius.")
    



    
    
    
    
    
    









        

    
