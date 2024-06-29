# Write a program and ask user to enter number, 5 times using while loop. store each value in list.
# calculate the sum of all values in a list.

# Solution :

my_list=[]

while len(my_list) < 5 :
    number = int(input("Enter number:"))
    my_list.append(number)

print("The sum of all values in a list", my_list, "is :",  sum(my_list))