def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_primes_in_range(start, end):
    """Display all prime numbers within a range."""
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

# Get user input for the range
start_range = int(input("Enter the start of the range: "))

# Check if the start number is negative
if start_range < 0:
    print("Enter a non-negative number.")
else:
    end_range = int(input("Enter the end of the range: "))
    
    # Check if the end number is less than the start number
    if end_range < start_range:
        print(f"Enter a number greater than {start_range}.")
    else:
        # Display prime numbers in the specified range
        display_primes_in_range(start_range, end_range)