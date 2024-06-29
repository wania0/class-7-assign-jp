# Write a program that takes user input and display it. The program keep ask user the input until user enters “0”

# Solution :

while True :
    user_input = int(input("Enter any number:"))
    if user_input == 0:
        print("Loop terminate")
        break
    print(user_input)