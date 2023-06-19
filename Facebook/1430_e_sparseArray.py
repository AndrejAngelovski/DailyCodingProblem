# You have a large array with most of the elements as zero.

# Use a more space-efficient data structure, SparseArray, that implements the same interface:

# init(arr, size): initialize with the original large array and size.
# set(i, val): updates index at i with val.
# get(i): gets the value at index i.

class SparseArray:
    def __init__(self, arr, size):
        self.size = size
        self._dict = {}
        for i, e in enumerate(arr):
            if e != 0:
                self._dict[i] = e

    def set(self, i, val):
        if i < 0 or i >= self.size:
            raise IndexError('Out of bounds')
        if val != 0:
            self._dict[i] = val
        elif i in self._dict:
            del self._dict[i]

    def get(self, i):
        if i < 0 or i >= self.size:
            raise IndexError('Out of bounds')
        return self._dict.get(i, 0)

def main():
    arr = list(map(int, input("Enter space-separated elements of array: ").split()))
    sparse_array = SparseArray(arr, len(arr))
    while True:
        print("Choose operation: \n 1. Set value \n 2. Get value \n 3. Exit")
        choice = int(input())
        if choice == 1:
            i = int(input("Enter index: "))
            val = int(input("Enter value: "))
            sparse_array.set(i, val)
        elif choice == 2:
            i = int(input("Enter index: "))
            print(sparse_array.get(i))
        elif choice == 3:
            break

if __name__ == "__main__":
    main()