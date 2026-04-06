#To print square pattern with alphabet symbols

#Output:
#Enter n value : 3
#A A A
#B B B
#C C C

#Enter n Value : 5
#A A A A A
#B B B B B
#C C C C C
#D D D D D
#E E E E E

#hint : Use the chr() function to convert ASCII values to characters. The ASCII value for 'A' is 65, so you can use chr(65 + i) to get the corresponding alphabet for each line, where i is the current line number starting from 0.


#Solution
n = int(input("Enter n Value : "))
for i in range(n):
    print((chr(65 + i) + " ") * n)  # This will print the current alphabet followed by a space, repeated n times for each line

# Time Complexity: O(n^2) because we have two nested loops, one for iterating through the alphabets from A to the nth alphabet and another for printing each alphabet n times = means we are printing n alphabets in each of the n lines, resulting in n * n = n^2 operations.
# Space Complexity: O(1) as we are not using any additional data structures that grow with the input size.