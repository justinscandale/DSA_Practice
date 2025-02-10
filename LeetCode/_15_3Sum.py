#  LINK TO PROBLEM:
#  https://leetcode.com/problems/3sum/

#  TAGS:
#  Two-Pointer, Set

#  SOLUTION:
#  We sort the array so we can use the two pointer method
#  We iterate through the array and for each element we search for pairs that add to the negative of the current element
#  We do this by using a two pointer approach where we move the left and right pointers until we find a pair that adds to the negative of the current element
#  We then add these pairs to a set to avoid duplicates
#  We then return the set as a list

# TIME COMPLEXITY:  O(n^2) - checks pairs in O(n) time for n-nums we get n^2
# SPACE COMPLEXITY:  O(n*logn) - sorting

def threeSum(nums:list[int]) -> list[list[int]]:
    #sort nums
    nums.sort()
    #iterate through all nums <= 0 to then search for pairs that add to 0 with them
    result = set()
    for index, num in enumerate(nums):

        if num>0:
            break

        target = abs(num)
        left = index+1
        right = len(nums)-1

        while(left<right):
            if target-nums[left]-nums[right]<0:
                    right -=1
            elif target-nums[left]-nums[right]>0:
                left += 1
            else:
                    result.add((num,nums[left],nums[right]))
                    left+=1

    return [list(res) for res in result]
				

#test
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
