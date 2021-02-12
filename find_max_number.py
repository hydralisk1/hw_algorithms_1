# Function to find max number
def max_number(*numbers):
    max = numbers[0]

    for i in numbers[1:]:
        max = i if i > max else max

    return max

try:
    first = int(input("Input the first number: "))
    second = int(input("Input the second number: "))
    third = int(input("Input the third number: "))

    print(f"The maximum number is {max_number(first, second, third)}.")

except ValueError:
    print("You have to input integer values")