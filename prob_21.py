# Write a function called get_highest that takes 2 numbers as parameters and returns the highest of the 2 numbers.

# Solution :

def get_highest(num_1,num_2):
    if num_1 > num_2 :
        return num_1
    else :
        return num_2

num_1 = int(input("Enter fisrt number:"))
num_2 = int(input("Enter Second number:"))

result = get_highest(num_1, num_2)

print("This highest number is :", result)

