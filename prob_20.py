# Write a function called is_divisable_by_11 that takes an integer as an parameter and returns whether it is divisible by 11 or not.

# Solution :

def is_divisable_by_11(a):
    if a % 11 == 0:
        print("Yes it is divisible by 11.")
    else:
        print("It is not divisible by 11.")
    return a 

a = int(input("Enter any number to check it is divisible by 11 or not:"))

is_divisable_by_11(a)
        
