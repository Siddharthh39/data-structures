from os import *
from sys import *
from collections import *
from math import *
import string

def ninjaGram(str):
    str = str.lower()
    return set(string.ascii_lowercase).issubset(Counter(str))

def main():
    str = input("Enter the string: ")
    print(ninjaGram(str))

if __name__ == "__main__":
    main()