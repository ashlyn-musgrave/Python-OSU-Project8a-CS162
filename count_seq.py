# Author: Ashlyn Musgrave
# GitHub Username: ashlyn-musgrave
# Date: 8/6/2023
# Description: This program writes a generator function named count_seq that doesn't require
# any arguments and generates a sequence that starts like this: 2, 12, 1112, 3112, 132112,
# 1113122112, 311311222112, 13211321322112

def count_seq():
    """
    Initialize the sequence with the first two terms
    """
    sequence = ['2', '12']

    while True:
        # Get the last term in the sequence
        prev_term = sequence[-1]

        # Initialize variables to store the next term
        next_term = ''
        count = 1

        # Calculate the next term based on the previous term
        for i in range(1, len(prev_term)):
            if prev_term[i] == prev_term[i - 1]:
                count += 1
            else:
                next_term += str(count) + prev_term[i - 1]
                count = 1

        # Add the last count and digit to the next term
        next_term += str(count) + prev_term[-1]

        # Append the next term to the sequence
        sequence.append(next_term)

        # Yield the next term
        yield next_term