# Ask user to input and convert to integer
input_number = int(input('Enter an integer greater than 3: '))

# Copy input to number
number = input_number

# Initialize variables
counter = 2
flag = False
separator = ''

# Run the loop if number > 1
while number > 1:

# Do if number can be divided by counter
    if number % counter == 0:

        # Print the header if factor is found for the first time and set the flag to true.
        if flag == False:
            print(f'The factor of {input_number} are [', end = '')
            flag = True

        # Print the separator and the number.
        print(f'{separator}{counter}', end = '')

        # Update the separator.
        separator = ', '

        # Update number by dividing counter, then reset counter to 2.
        number /= counter
        counter = 2
        
    # If number can't be divided.
    else:

        # Print the prime number message if counter is equal to input_number - 1 and quit the while loop.
        if counter == input_number - 1:
            print(f'{input_number} is a prime number.')
            break
        
        # If the counter doesn't reach the input_number - 1, increment counter by 1.
        else:
            counter += 1

# Print the ending square bracket if flag is true.
if flag == True:
    print(']')
