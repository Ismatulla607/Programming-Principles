import random
import math

# 1 ounces
def to_gramm(ounces):
    return ounces * 28.3495

# 2 Fahrenheit temperature
def toC(fahrenheit):
    return (fahrenheit - 32) * 5/9

# 3 Puzzle
def solve(numheads, numlegs):
    rabs = (numlegs - 2*numheads)//2
    chicks = numheads - rabs
    return rabs, chicks

# 4 Prime
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 5 KBTU
def perm(str):
    if len(str) == 1:
        return str
    lst = []
    for i in range(len(str)):
        for j in perm(str[:i]+str[i+1:]):
            lst.append(str[i]+j)
    return lst

# 6 Inverse
def inverse(s):
    return s[::-1]

# 7 33 
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# 8 Spy game
def spy_game(lst):
    zer = 0
    for i in lst:
        if i == 0:
            zer+=1
        elif i == 7 and zer == 2:
            return True
    return False

# 9. Radius
def vol(r):
    return (4/3) * 3.14159 * r**3

# 10 Set
def uniquelist(lst):
    return list(set(lst))

# 11 Palindrome
def pol(s):
    return s == s[::-1]

# 12 Histogram
def his(lst):
    for i in lst:
        print('*' * i)

# 13 Guess the number

def chislo():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    number = random.randint(1, 20)
    guesses = 0
    
    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
