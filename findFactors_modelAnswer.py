'''
Program name: findFactors_modelAnswer.py

Variable lists:-
    inputText: str  (String format of user's input)
    number: int (User's input in integer format, divided by the smallest prime factor when it is found)
    factor: int (Smallest prime factor of number. If factor is 0 after the loop, number is a prime number)
    found: bool (Set to True when prime factor for number is found)
    numberRange: int (First round of loop = (2 to number - 1), after that loop = (2 to number))

Abstraction:-
    -> 7 is a prime number. It can't be divided perfectly by 2 ~ 6.
    -> 12 is not a prime number. There are two combinations of factors (2 * 6) and (2 * 2 * 3). 
    We will take second combination to get the 'smallest' number of factors.
    -> The idea is to start the loop from 2 and record the smallest factor and ignore the rest.
    -> Take 14 as example, first factor is 2 and the second one is 7.
    14 / 2 = 7
    7 / 7 = 1
    When the number become 1, the calculation is done.

Program structure explaination:-
    -> First loop: while number > 1 (To determine whether the calcuation is done or not)
    -> Second loop: for i in range(2, numberRange) 
    (Loop from 2 to number for the first time, after that loop until number + 1)
    -> If no factor is found in Second loop for the first time, it's a prime number.

Remark:-
    This program is not the most efficient way to calculate the result. It is suggusted that
    candidates should write your own version with the smarter method.
'''

# Ask for user's input
inputText = input("Enter an integer greater than 3: ")

# Initialize variables
number = int(inputText)
factor = 0

# End program when number is 1
while number > 1:

    # Set flag to false
    found = False

    # Set the final number of the for loop
    if number == int(inputText):
        numberRange = number
    else:
        numberRange = number + 1

    # Loop through the number
    for i in range(2, numberRange):

        # Run if remainder is 0 and flag is false
        if number % i == 0 and found == False:

            # Print '[' ONLY if factor is 0
            if factor == 0:
                print('[', end = '')

            # Set factor to 1 and set flag to true
            factor = i
            found = True      

    # Run if factor is greater than 1
    if factor > 1:

        # Print factor and divide number with factor
        print(factor, end = '')
        number //= factor

        # Run if number is 1 after the division (End of calculation)
        if number == 1:
            print(']')

        # Else print ',' if number > 1 
        else:
            print (', ', end= '')

    # Print message if factor is less than 2 and set number to 1 in order to quit the program.
    else:
        print('This is a prime number')
        number = 1