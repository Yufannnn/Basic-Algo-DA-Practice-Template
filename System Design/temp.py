def maximal_unique_odd_sum_decomposition(n):
    # List to hold the odd numbers forming the sum decomposition
    sum_decomposition = []
    # Variable to keep track of the current sum of the decomposition
    current_sum = 0
    # Starting with the smallest odd number
    next_odd_number = 1

    # Loop to add odd numbers to the decomposition
    while True:
        # Check if adding the next odd number exceeds 'n'
        if current_sum + next_odd_number > n:
            break
        # Add the odd number to the decomposition and update the current sum
        sum_decomposition.append(next_odd_number)
        current_sum += next_odd_number
        # Move to the next odd number
        next_odd_number += 2

    # Adjust the last number if the sum does not equal 'n'
    if current_sum < n:
        # Calculate the last number needed to make the sum equal to 'n'
        # This step replaces the last number in the list with the correct value to ensure the sum equals 'n'
        last_number_needed = n - (current_sum - sum_decomposition[-1])
        sum_decomposition[-1] = last_number_needed

    return sum_decomposition

# Example usage:
n = 15
print(maximal_unique_odd_sum_decomposition(n))
