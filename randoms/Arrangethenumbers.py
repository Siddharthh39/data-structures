def maximumSubarraySum(v: list[int]) -> int:
    storePos = []

    for i in range(len(v)):
       if v[i] >= 0:
          storePos.append(v[i])
    
    return sum(storePos)

def main():
   v = [int(x) for x in input("Enter the numbers: ").split()]
   print(maximumSubarraySum(v))

if __name__ == "__main__":
   main()