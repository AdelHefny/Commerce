# Task 3

#               Name             |      id       |         Problems

# Adel ahmed Mohamed El hefny    |   20230198    |  Problem 1  & Problem 2

# Mohamed Khaled Gamal El-Deen   |   20230595    |  Problem 3  & Problem 4

# Ahmed Mohamed Mahmoud Ahmed    |   20230598    |  Problem 5  & Problem 6




from math import sqrt

def Problem_1():
    # Loop until a valid number is entered
    while True:
        try:
            mark = float(input("Please insert a number: "))
            break
        except ValueError:
            # If conversion fails, display an error message
            print("Invalid input. Please enter a valid number.")
            continue

    # Determine the grade based on the entered mark
    if mark >= 90:
        print("A+")
    elif mark < 90 and mark >= 85:
        print("A")
    elif mark < 85 and mark >= 80:
        print("B+")
    elif mark < 80 and mark >= 75:
        print("B")
    elif mark < 75 and mark >= 70:
        print("C+")
    elif mark < 70 and mark >= 65:
        print("C")
    elif mark < 65 and mark >= 60:
        print("D+")
    elif mark < 60 and mark >= 50:
        print("D")
    else:
        print("F")
    return

def Problem_2():
    # Loop until a valid number is entered
    while True:
        try:
            num = int(input("Please insert a number: "))
            break
        except ValueError:
            # If conversion fails, display an error message
            print("Invalid input. Please enter a valid integer.")
            continue

    # Convert the number to a string to iterate over its digits
    num_str = str(num)
    power = len(num_str)
    power_sum = 0

    # Calculate the sum of powers of each digit
    for digit in num_str:
        power_sum += pow(int(digit), power)

    # Check if the sum of powers equals the original number
    if power_sum == num:
        print("It's an Armstrong number.")
    else:
        print("It's not an Armstrong number.")
    return

def Problem_3():
    # Welcome message
    print("Welcome to Pi Finder")

    n = "-1" # Take a valid positive number from the user
    while not(n.isdigit()):
        n = input("Please enter an integer: ")
    n = int(n)

    pi = 0.0 # initialize the pi variable with zero
    for i in range(0,n):
        # loop from 0 to n-1 and apply the rule then add the value to the variable pi
        pi = pi + 1/(pow(-1,i) * (2*i+1))
    print("The value of Pi in from the first",n,"terms is :",pi*4)
    return

def Problem_4():
    # print welcome message and take a sentence from the user and
    print("Welcome to Data Encryptor tool")
    s = input("Enter your sentence : \n")
    encr = ""
    for c in s: # loop over each character in the sentence
        # Encryption method and conditions
        if c == 'z':
            encr += 'a'
        elif c == 'Z':
            encr += 'A'
        elif c == '9':
            encr += '0'
        elif (c < 'z' and c >= 'a') or (c < 'Z' and c >= 'A') or (c >= '0' and c < '9'):
            encr += chr(ord(c) + 1)
        else:
            encr += c # sympol or space then no change


    print(encr) # print the encrypted sentence
    return

def Problem_5():
    # ask the user to enter elements for list 1 and store them as a list
    list1 = input("Enter elements of list 1: ").split()
    list1 = [int(x) for x in list1]
    # ask the user to enter elements for list 2 and store them as a list
    list2 = input("Enter elements of list 2: ").split()
    list2 = [int(x) for x in list2]

    # Initialize the flag to True
    flag = True

    # Check if the lengths of the two lists are equal
    if len(list1) != len(list2):
        # If the lengths are not equal, set the flag to False
        flag = False
    else:
        # If the lengths are equal, iterate through the elements of list1
        for element in list1:
            # Check if the current element of list1 is found in list2
            if element in list2:
                # If element in list1 is found in list2, remove the matched element from list2
                list2.remove(element)
            else:
                # If element in list1 is not found in list2, set the flag to False and break out of the loop
                flag = False
                break

    # Print "True" if flag is True, indicating that the two lists contain the same elements, otherwise print "False"
    print("two lists are equal" if flag else "lists are not equal")
    return

def Problem_6():
    # ask the user to enter a number for which the factorial is to be calculated
    number = int(input("Enter your number you want to know his factors: "))
    # the code will loop from 1 to sqrt of the number this is because any number has two factors before and after square
    # root if they are multiplied the result will be the number
    limit = int(sqrt(number)) + 1

    # Iterate through the range of numbers from 1 to the limit
    for i in range(1, limit, 1):
        # Check if the current number before square root is a factor of the input number
        if number % i == 0:
            # If it is a factor, print it (factor before square root )
            print(i)
            # this check to not print root of squares twice
            # check of number before sqrt not equal number after sqrt
            if i != number // i:
                # print factor after square root
                print(number // i)
    return

def determine_problem(choice):
    print('\n' * 49) # Print 50 enters to separate between each trail

    # call the required problem according to the user choice
    if choice == '1':
        Problem_1()
    elif choice == '2':
        Problem_2()
    elif choice == '3':
        Problem_3()
    elif choice == '4':
        Problem_4()
    elif choice == '5':
        Problem_5()
    elif choice == '6':
        Problem_6()

    return

stat_choice = '2'
print("Welcome!") # Main Welcome message

while stat_choice != '3':

    problem_choice = '8'


    # Take valid input that refers a problem form the 6 problems
    while not (problem_choice <= '6' and problem_choice >= '1'):
        print('\n'*2)
        print('''Currented Programms
        1. Problem 1 ( Marks to grades converter )
        2. Problem 2 ( Armstrong number checker )
        3. Problem 3 ( Find Pi by first nth terms of Leibniz formula )
        4. Problem 4 ( Data Encryptor )
        5. Problem 5 ( Equavilent lists checker )
        6. Problem 6 ( Factors of a given number )''' )
        problem_choice = input("Please enter a VALID choice (number form 1 to 6): ")


    stat_choice = '1'
    while stat_choice == '1':

        determine_problem(problem_choice)

        stat_choice = '5'
        print('\n' * 2)

        # Detect if the user want to continue in the same problem or other or to close the whole prograam
        while stat_choice != '1' and stat_choice != '2' and stat_choice != '3':
            print('''Do you want to continue?
            1. Yes, The same subprogram
            2. Yes, but other subprogram
            3. No, Close the program''')
            stat_choice = input("Please enter a VALID choice (1,2,3): ")
