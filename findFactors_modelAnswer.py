inputText = input("Enter an integer greater than 3: ")
number = int(inputText)

factor = 0
while number > 1:
    found = False
    if number == int(inputText):
        numberRange = number
    else:
        numberRange = number + 1
    for i in range(2, numberRange):
        if number % i == 0 and found == False:
            if factor == 0:
                print('[', end = '')
            factor = i
            found = True      
    if factor > 1:
        print(factor, end = '')
        number //= factor
        if number == 1:
            print(']')
        else:
            print (', ', end= '')
        factor = 1
    else:
        print('This is a prime number')
        number = 1