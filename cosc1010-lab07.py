# Chauncy Hendon
# UWYO COSC 1010
# 10/31/24
# Lab 7
# Lab Section: 12 
# Sources, people worked with, help given to: 
# your
# comments
# here


# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

factorial = 1
factorial_calc= 1
fac_true = True

while fac_true:
    factorial_input = input("Give a positive number to then be facorialed: ")
    if factorial_input.isdigit() == True:
        factorial = int(factorial_input)
        factorial_calc = int(factorial_input)
        while factorial > 1:
            factorial_calc = factorial_calc * (factorial-1)
            factorial -= 1
        fac_true = False
    else:
        print("Please input a positive number instead")


print(f"The result of the factorial based on the given bound is {factorial_calc}")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

num_sum = 0 
fixed_input = ""
user_i_list = []
is_neg = False
is_number = True

while True:
    user_input = input("Please give a positive or negative value, type exit to leave: ")

    fixed_input = ""
    is_neg = False
    user_i_list = []
    is_number = True

    if user_input == "exit":
        break

    for value in user_input:
        user_i_list.append(value)

    if user_i_list[0].isdigit():
        is_number = True
    elif user_i_list[0] == "-":
        is_neg = True
    else:
        is_number = False
        print("Input a number next time")

    for i in user_i_list[1:]:
        if i.isdigit() != True:
            print("Please input a number next time")
            is_number = False
            
    if is_number:
        if user_i_list[0]== "-":
            is_neg = True
            for i in user_i_list[1:]:
                fixed_input = fixed_input + i
        else:
            for i in user_i_list:
                fixed_input = fixed_input + i

        if is_neg:
            num_sum += -int(fixed_input)
        else:
            num_sum += int(fixed_input)

print(f"Your final sum is {num_sum}")


print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 

operators_list = ["+","-","/","*","%"]
calculator_input = input("Give an operand operator operand statement: ")
operator_used = ""
final_problem = None
final_problem_split = ""
result = None
number_of_nums = 0

for item in calculator_input:
    if item.isdigit():
        number_of_nums += 1
    for operator in operators_list:
        if item == operator:
            operator_used = operator

if number_of_nums >= 2:
    number_of_nums = 0

    #+
    if operator_used == "+":
        final_problem = calculator_input.split("+")
        for item in final_problem:
            final_problem_split += item
        final_problem_split = final_problem_split.split()
        print(final_problem_split)

        for item in final_problem_split:
            if item.isdigit():
                number_of_nums += 1
        if number_of_nums == 2:
            result = int(final_problem_split[0]) + int(final_problem_split[1])
        else:
            print("Please input an operand operator operand statement")

    #-
    if operator_used == "-":
        final_problem = calculator_input.split("-")
        for item in final_problem:
            final_problem_split += item
        final_problem_split = final_problem_split.split()
        print(final_problem_split)

        for item in final_problem_split:
            if item.isdigit():
                number_of_nums += 1
        if number_of_nums == 2:
            result = int(final_problem_split[0]) - int(final_problem_split[1])
        else:
            print("Please input an operand operator operand statement")

    #*
    if operator_used == "*":
        final_problem = calculator_input.split("*")
        for item in final_problem:
            final_problem_split += item
        final_problem_split = final_problem_split.split()
        print(final_problem_split)

        for item in final_problem_split:
            if item.isdigit():
                number_of_nums += 1
        if number_of_nums == 2:
            result = int(final_problem_split[0]) * int(final_problem_split[1])
        else:
            print("Please input an operand operator operand statement")

    #/
    if operator_used == "/":
        final_problem = calculator_input.split("/")
        for item in final_problem:
            final_problem_split += item
        final_problem_split = final_problem_split.split()
        print(final_problem_split)

        for item in final_problem_split:
            if item.isdigit():
                number_of_nums += 1
        if number_of_nums == 2:
            result = int(final_problem_split[0]) / int(final_problem_split[1])
        else:
            print("Please input an operand operator operand statement")

    #%
    if operator_used == "%":
        final_problem = calculator_input.split("%")
        for item in final_problem:
            final_problem_split += item
        final_problem_split = final_problem_split.split()
        print(final_problem_split)

        for item in final_problem_split:
            if item.isdigit():
                number_of_nums += 1
        if number_of_nums == 2:
            result = int(final_problem_split[0]) % int(final_problem_split[1])
        else:
            print("Please input an operand operator operand statement")

print("The result of your calculation is:")
print(result)

    





        