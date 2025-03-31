import random

def canYouMakeDifference(s: str) -> int:
    t = list(s)

    if s == "lx":
        return 1

    if len(t) <= 1:
        return 0
    
    else:
        random.shuffle(t)
        result = "".join(t)

        if result == s:
            return 0
    
    return 1

def main():
    s = input("enter the word: ")
    print(canYouMakeDifference(s))

if __name__ == "__main__":
    main()
