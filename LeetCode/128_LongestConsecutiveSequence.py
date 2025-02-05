#  LINK TO PROBLEM:
# https://leetcode.com/problems/longest-consecutive-sequence/description

#  TAGS:
#  HASMAPS || ARRAYS 

#  SOLUTION:
# This solution will use a two pass method
# The first pass will put each element in the array into a set
# The second pass will first check if at element i, elem[i]+1 is in the array
# if this element exsists it means that this element is not the largest in a sequence
# for every element i we find that where element[i]+1 is not in the set,  we check the set for element-1, then element-2...
# until we see how long that sequence is updating maxlen as we go

# TIME COMPLEXITY:  O(n)
# SPACE COMPLEXITY:  O(n)

def lc(nums: list[int]) -> int:

    numSet = set(nums)
    maxlen = 0

    for num in nums:
        curlen = 1
        if num+1 not in numSet:
            while num-curlen in numSet:
                curlen +=1

        maxlen = max(maxlen,curlen)
    
    return maxlen
        

#testing code
input = [1,11,2,12,3,14,4,15]
print(lc(input))