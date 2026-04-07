# To print Pyramid pattern with * symbols

# Output:
# Enter n value : 3
#   *
#  * *
# * * *

# Enter n Value : 5
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# Hint: Use nested loops to print the pattern. The outer loop will handle the number of rows, and the inner loop will handle the number of spaces and stars in each row.    

# Solution - 1

n = int(input("Enter n Value : "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)  # This will print the required number of spaces followed by the required number of stars for each row      

# Time Complexity: O(n^2) because we have two nested loops, one for iterating through the rows and another for printing the spaces and stars in each row.
# Space Complexity: O(1) as we are not using any additional data structures that grow with the input size.

# Solution - 2

n = int(input("Enter n Value : "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")  # This will print the required number of spaces without moving to a new line
    for k in range(i):
        print("* ", end="")  # This will print the required number of stars followed by a space, without moving to a new line
    print()  # This will move to the next line after printing the spaces and stars for the current row

# Time Complexity: O(n^2) because we have two nested loops, one for iterating through the rows and another for printing the spaces and stars in each row.
# Space Complexity: O(1) as we are not using any additional data structures that grow with the input size.

