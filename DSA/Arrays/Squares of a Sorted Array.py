# Question

# You are given an array of Integers in which each subsequent value is not less than the previous value. 
#Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.


#1) Understand the Question 
# lets say arr=[1,2,3,4,5]
# each subsequent value is not less than the previous value.==> numbers should be in Ascending order / non decreasing order
# we have to return a new array with the squares of each number sorted in ascending order.

#Ask clarifying questions if any
# Can the input array contain negative numbers?
# Yes, the input array can contain negative numbers. The function should handle negative numbers correctly by squaring them and ensuring the resulting array of squares is sorted in ascending order.
#Can the input array contain duplicate numbers?
# Yes, the input array can contain duplicate numbers. The function should handle duplicates correctly by including the squares of all occurrences in the resulting array.
#Can the input array be empty?
# Yes, the input array can be empty. In this case, the function should return an empty array as well.
#Can the input array contain zero?
# Yes, the input array can contain zero. The function should handle zero correctly by including its square (which is zero) in the resulting array.
#Can the input array contain non-integer values?
# No, the input array should only contain integers. The function is designed to work with integer values, and non-integer values would not be valid input for this problem.
#Can the input array contain very large integers?
# Yes, the input array can contain very large integers. The function should be able to handle large integers without any issues, as Python's integer type can grow as needed to accommodate large values.   

#Brute Force Approach:
#1) Create a new array to store the squares of the numbers.
#2) Iterate through the input array, square each number, and append it to the new array.
#3) Sort the new array in ascending order.
#4) Return the sorted array.

#brute force approach code:

def sorted_array(arr):
    # Step 1: Create a new array to store the squares of the numbers - space complexity O(n) for the new array
    squares = []
    
    # Step 2: Iterate through the input array, square each number, and append it to the new array - TC O(n)
    for num in arr:
        squares.append(num ** 2)
    
    # Step 3: Sort the new array in ascending order - TC O(n log n) due to sorting
    squares.sort()
    
    # Step 4: Return the sorted array Total Time Complexity: O(n log n) due to sorting step
    return squares

input_array = [-4, -1, 0, 3, 10]
result = sorted_array(input_array)
print(result)  # Output: [0, 1, 9, 16, 100] 