from collections import Counter

def specificOrder(x: str, y: str):
    freq = Counter(x)
    result = []

    for ch in y:
        if ch in freq:
            result.append(ch * freq[ch])
            del freq[ch]

    for ch, count in freq.items():
        result.append(ch * count)

    return "".join(result)

def main():
    x = input("Enter the first string: ")
    y = input("Enter the second string: ")
    
    print(specificOrder(x, y))
    

if __name__ == "__main__":
    main()
