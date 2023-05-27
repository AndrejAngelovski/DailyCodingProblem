# A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

# For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.

def find_fixed_point(arr):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < mid:
            low = mid + 1
        elif arr[mid] > mid:
            high = mid - 1
        else:
            return mid
        
    return False

def main():
    arr = list(map(int, input("Enter the elements of the array, separated by spaces: ").split()))
    fixed_point = find_fixed_point(arr)
    if fixed_point:
        print("The fixed point is:", fixed_point)
    else:
        print("There is no fixed point in the array.")

if __name__ == "__main__":
    main()