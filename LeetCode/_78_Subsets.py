#  LINK TO PROBLEM:
#  https://leetcode.com/problems/subsets/

#  TAGS:
#  BACKTRACKING

#  SOLUTION:
#  For each element in array we either include it in the subset or not
#  To get every possible subset we must see all combinations
#  We use backtracking to solve this 
#  We start at a index 0 and see both possibilites (include it or dont)
#  Then for both of those we go to index 1 and include both possibilites (take index 1 or not)
#  We continue this until we get to the last index of the input array which gives us all subsets

# TIME COMPLEXITY:  O(n * 2^n)
# SPACE COMPLEXITY:  O(n)

def subsets(nums: list[int]) -> list[list[int]]:

    res = [[]]  # list to store subsets
    
    #depth first search algorithm to add a new subset that includes nums[i] to every subset in res
    def dfs(i):
        if i < len(nums):
            for j in range(len(res)):
                new_subset = res[j].copy()
                new_subset.append(nums[i])
                res.append(new_subset)

            dfs(i+1)
        
    dfs(0) #Call dfs 

    return res

#testing code
input = [1,2,3]
print(subsets(input))