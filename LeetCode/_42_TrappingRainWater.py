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

def trap1(heights: list[int]) -> int:

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

# Solution 2 which uses a similar approach but two passes, one for the left sum and one for the right sum
# This is a slower than the first solution but is still O(n)
def trap2(heights: list[int]) -> int:
    if not heights:
        return 0

    res = 0

    #find vol based on left max height
    cur_vol = 0
    left_max = heights[0] 
    for left in heights:
        print(f"LEFTMAX {left_max}, LEFT {left}, CURVOL {cur_vol}")
        if left_max >  left:
            cur_vol += left_max - left
        else:
            res += cur_vol
            cur_vol = 0
            left_max = left

    #find volumes based on righht max height
    cur_vol = 0
    right_max = heights[len(heights)-1] 
    for right in heights[::-1]:
        if right_max >=  right:
            cur_vol += right_max - right
        else:
            res += cur_vol
            cur_vol = 0
            right_max = right

    return res
            


#testing code
input = [0,2,0,3,1,0,1,3,2,1]
print(trap2(input))
input=[0,1,0,2,1,0,1,3,2,1,2,1]
print(trap2(input))