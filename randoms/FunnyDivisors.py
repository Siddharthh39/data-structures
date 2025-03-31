def findSum(n, arr):
    size = len(arr)
    store = []

    for i in range(size):
        if arr[i] % 2 == 0 or arr[i] % 3 == 0:
            store.append(arr[i])
    
    return sum(store)


def main():
    arr = [int(x) for x in input("Enter the array: ").split()]
    n = len(arr)
    print(findSum(n, arr))

if __name__ == "__main__":
    main()