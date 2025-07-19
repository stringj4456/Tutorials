import math

num_list = [10, -5, 1.2, "apple"]

print("This is the list we are testing:", num_list, "\n")

for num in num_list:
    try:
        num_factorial = math.factorial(num)
    except TypeError:
        print("Factorial is not supported for the given input type:", num)
    except ValueError:
        print("Factorial only accepts positive integer values.", num, "is not a positive integer")
    else:
        print("The factorial of", num, "is", num_factorial)
    finally:
        print("We are done now.\n")
