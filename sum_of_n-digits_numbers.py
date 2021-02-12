from random import randint

# Function that returns sum of a list that consists of numbers from each place value
def sum_of_n_digits(num):
    return sum([int(c) for c in str(num)])

# If the input value from user is not int, print error message.
try:
    digit = int(input("How many digit random number do you want: "))

    # if user input is less than or equal to 0, raise exception
    if digit <= 0:
        raise ValueError

    # create an n-digits random number
    num = randint(10**(digit-1), (10**digit)-1)

    # print the result
    print(f"{digit} digit random number is {num}.")
    print(f"Total of the numbers in each place value is {sum_of_n_digits(num)}.")

except ValueError:
    print("You have to input an integer value greater than 0.")