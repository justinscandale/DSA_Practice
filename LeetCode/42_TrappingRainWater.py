#  LINK TO PROBLEM:
#  https://leetcode.com/problems/trapping-rain-water/description/

#  TAGS:
#  Two-Pointer

#  SOLUTION:
# We start with one pointer at left = 0 and the other at right = len(input)-1
# We store left_max and right_max which represent the max value of whats been searched on the left and right side of the array
# We move left or right towards the center of the array, whichever has a smaller max height and then adjust the max to the new position
# In the new position we add the (new_max - value at pos) into the res variable  
# When the left and right pointers meet we have succesfully calculated the max volume for the entire array

# TIME COMPLEXITY:  O(n)
# SPACE COMPLEXITY:  O(1)

def trap(heights: list[int]) -> int:

    if not heights:
        return 0
    
    left = 0
    right = len(heights)-1
    left_height = heights[left]
    right_height = heights[right]
    res = 0

    while left < right:

        if left_height < right_height:
            left += 1
            left_height = max(left_height, heights[left])
            res += left_height - heights[left]
        else:
            right -= 1
            right_height = max(right_height, heights[right])
            res += right_height - heights[right]

    return res

#testing code
input = [0,2,0,3,1,0,1,3,2,1]
print(trap(input))