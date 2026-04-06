#Patttern -3
#To print square pattern with provided fixed digit in every row

#Output:
#Enter n value : 3
#1 1 1
#2 2 2
#3 3 3

#Enter n Value : 5
#1 1 1 1 1
#2 2 2 2 2
#3 3 3 3 3
#4 4 4 4 4
#5 5 5 5 5

#Solution - 1

n = int(input("Enter n Value : "))
for i in range(1, n + 1):
    print((str(i) + " ") * n)  # This will print the current number followed by a space, repeated n times for each line

# Time Complexity: O(n^2) because we have two nested loops, one for iterating through the numbers from 1 to n and 
# another for printing each number n times = means we are printing n numbers in each of the n lines, resulting in n * n = n^2 operations.
# Space Complexity: O(1) as we are not using any additional data structures that grow with the input size.

#Solution - 2

n = int(input("Enter n Value : "))
for i in range(1, n + 1):
    for j in range(n):
        print(i, end=" ")  # This will print the current number followed by a space, without moving to a new line
    print()  # This will move to the next line after printing n numbers

# Time Complexity: O(n^2) because we have two nested loops, one for iterating through the numbers from 1 to n and another for printing each number n times = means we are printing n numbers in each of the n lines, resulting in n * n = n^2 operations.
# Space Complexity: O(1) as we are not using any additional data structures that grow with the input size.