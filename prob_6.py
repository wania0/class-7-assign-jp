# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."

# Solution:

while True :
    name_input = input("Enter any name:").upper()
    print(name_input)
    if name_input == "END":
        break
    
print ("I am done")