# hollow square picture :

# Solution :

print("The pattern of hollow sqaure is given below:")

for i in range(0,5):
    for j in range(0,5):
        if i == 0 or i == 4 or j == 0 or j == 4 :
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()