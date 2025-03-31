class Solution:
    def matchSpecificPattern(self, words, pattern):
        hashmap = {}
        assigned_values = set()

        if len(words) != len(pattern):
            return "not valid"
        
        for i in range(len(words)):
            key = pattern[i]
            value = words[i]

            if key in hashmap:
                if hashmap[key] != value:
                    return "not valid"
            else:
                if value in assigned_values:
                    return "not valid"
                hashmap[key] = value
                assigned_values.add(value)
        
        return "valid"

def main():
    words = input("Enter the word: ")
    pattern = input("Enter the second word: ")

    sol = Solution()
    result = sol.matchSpecificPattern(words, pattern)
    
    print(result) 

if __name__ == "__main__":
    main()
