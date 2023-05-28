# We say a number is sparse if there are no 
# adjacent ones in its binary representation.
# For example, 21 (10101) is sparse, but 22 (10110)
# is not. For a given input N, find the smallest 
# sparse number greater than or equal to N.
# Do this in faster than O(N log N) time.

def nextSparse(x):
    binary = bin(x)[2:] # Convert binary into string removing the first two characters
    binary = list(binary[::-1]) # Reverse string and convert it into list

    last_final = 0 # To store last found final bit
    n = len(binary)

    # Start from second bit (next to LSB)
    # for i in range (1, n):
