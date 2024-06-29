# Write a function called km_to_miles that takes kilometers as a parameter, converts it into miles and returns the result.

# Solution :

def km_to_miles(km):
    miles = km * 0.621371
    return miles

km = int(input("Enter any km value to convert into miles:"))

result = km_to_miles(km)

print("The value of", km, "km in miles is equal to:", result, "miles")