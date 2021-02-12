def count_odd_and_even_numbers(number):
    num_of_odd = len([c for c in str(number) if (int(c) % 2) == 1])
    return {"num_of_odd": num_of_odd, "num_of_even": len(str(number))-num_of_odd}

try:
    count = count_odd_and_even_numbers(int(input("Input a number: ")))
    print(f"The number of odd digits: {count['num_of_odd']}")
    print(f"The number of even digits: {count['num_of_even']}")

except ValueError:
    print("You have to input an integer value")