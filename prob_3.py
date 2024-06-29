# consider the number 2783, the number consists of 4 digits.
# Count the total number of digits in a number using while loop.
# instruction (hint):
# x = 2783
# counter = 0
# run while loop as long as x becomes 0
# increment the counter inside while loop
# divide x by 10 using floor division syntax "//"

# Solution:

x = 2783
counter = 0

while x > 0 :
    x = x // 10
    counter += 1
    
print("Total number of digits in a number is: ", counter)