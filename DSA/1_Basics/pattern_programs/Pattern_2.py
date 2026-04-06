# Pattern - 2

#Square Pattern

#Output:
#Enter n value : 3
#* * *
#* * *
#* * *

#Enter n Value : 5
#* * * * *
#* * * * *
#* * * * *
#* * * * *
#* * * * *

# Solution

# Hint= Use the * operator with string, string multiplication

n = int(input("Enter n Value : "))
for i in range(n):
    print("* " * n)  # This will print n asterisks followed by a space, repeated n times for each line


