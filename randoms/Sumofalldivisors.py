def sumOfAllDivisors(n: int) -> int:
    total = 0
    store = []

    for i in range(1, n+1):
        total += (n // i) * i
    return total

def main():
    n = int(input("Enter the number"))
    print(sumOfAllDivisors(n))

if __name__ == "__main__":
    main()