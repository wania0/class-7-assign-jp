# Right traingle picture :
    
# Solution :

print("The pattern of right triangle is given below:\n")

for i in range(0,5): # 0,1,2,3,4
    for j in range(i,5): 
        print(" ", end=" ")
    for j in range(0,i+1):
        print("*", end=" ")
    print()