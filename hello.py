def is_armstrong(n):
    # Convert the number to a string to easily extract digits
    digits = [int(d) for d in str(n)]
    # Calculate the sum of the cubes of each digit
    sum_cubes = sum([d ** len(str(n)) for d in digits])
    # Return True if the sum of cubes is equal to the original number, False otherwise
    return sum_cubes == n

# Test the function
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

