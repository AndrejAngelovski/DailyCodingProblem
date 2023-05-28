# Write a function that returns the bitwise AND of all integers between M and N, inclusive.
def rangeBitwiseAnd(M, N):
    shift = 0
    while M != N:
        M >>= 1
        N >>= 1
        shift += 1
    return M << shift

def main():
    M = 5
    N = 7
    print(rangeBitwiseAnd(M, N))

if __name__ == "__main__":
    main()