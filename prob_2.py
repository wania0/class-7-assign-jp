# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# output:
# {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1, "f": 1, "g": 1, "h": 1}
# hint: use nested loop

# Solution:

l1 = ['a', 'b', 'c', 'd']
l2 = ['e', 'b', 'g', 'd', 'f', 'h']

new_dict = {}

for item in l1:
    
    if item not in new_dict:
        new_dict[item] = 1
    else:
        new_dict[item] += 1
       

for item in l2:

    if item not in new_dict:
        new_dict[item] = 1
    else:
        new_dict[item] += 1
        
        
print(new_dict)

