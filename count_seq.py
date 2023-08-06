# Author: Ashlyn Musgrave
# GitHub Username: ashlyn-musgrave
# Date: 8/6/2023
# Description: This program writes a generator function named count_seq that doesn't require
# any arguments and generates a sequence that starts like this: 2, 12, 1112, 3112, 132112,
# 1113122112, 311311222112, 13211321322112.

def count_seq():
    """
    Initializes the sequence with the first two terms
    """
    sequence = ['2', '12']

    # Yield the first two terms
    yield sequence[0]
    yield sequence[1]

    while True:
        # Initialize variables to store the next term
        next_term = ''
        current_digit = sequence[-1][0]
        count = 1

        # Iterate through the digits of the previous term
        for i in range(1, len(sequence[-1])):
            if sequence[-1][i] == current_digit:
                # If the current digit is the same as the previous one, increment count
                count += 1
            else:
                # Append the count and the previous digit to the next term
                next_term += str(count) + current_digit

                # Update variables for the next digit
                current_digit = sequence[-1][i]
                count = 1

        # Append the count and the last digit to the next term
        next_term += str(count) + current_digit

        # Yield the next term as a string
        yield next_term

        # Append the next term to the sequence for the next iteration
        sequence.append(next_term)
