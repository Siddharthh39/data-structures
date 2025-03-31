def flipSomeBits(num, arr, n):
    binary_str = format(num, 'b')
    binary_list = list(binary_str)
    length = len(binary_list)

    for idx in arr:
        pos = length - idx        
        if 0 <= pos < length:
            
            if binary_list[pos] == '1':
                binary_list[pos] = '0'
            
            else:
                binary_list[pos] = '1'

    return int(''.join(binary_list), 2)

def main():
    num = int(input("Enter the number: "))
    arr = list(map(int, input("Enter the array: ").split()))
    print(flipSomeBits(num, arr, len(arr)))

if __name__ == "__main__":
    main()
