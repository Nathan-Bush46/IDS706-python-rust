import time

def sum_of_squares(numbers):
    return sum(x * x for x in numbers)

# Sample data
numbers = list(range(1_000_000))
# Timing the function
start_time = time.time()
result = sum_of_squares(numbers)
end_time = time.time()

print("Sum of squares:", result)
print("Time taken (seconds):", end_time - start_time)
