# Write a function called fuel_cost that takes 2 numbers as parameter "distance" as required arg 
# and "fuel_per_liter" as optional arg that has default value to 280. 
# The function should return the cost in Rs.

# Solution :

def fuel_cost(distance, fuel_per_liter = 280 ):
    cost = distance * fuel_per_liter
    return cost

distance = float(input("Enter the distance travelled:"))

result = fuel_cost(distance)

print("The fuel cost for traveling", distance, "km is: Rs.", result)