#  LINK TO PROBLEM:
#  https://leetcode.com/problems/climbing-stairs/description/

#  TAGS:
#  Dynamic Programming 1D

#  SOLUTION:
#  We use a cache to store the number of ways to climb to each step
#  We start with 1 way to climb 1 step and 2 ways to climb 2 steps
#  We then iterate through the rest of the steps and add the number of ways to climb to the current step to the number of ways to climb to the next step
#  We return the number of ways to climb to the last step  
#  This is very similar to the fibonacci sequence

# TIME COMPLEXITY:  O(n)
# SPACE COMPLEXITY:  O(n)


def climbStairs(n: int) -> int:
    
    cache = [0] * n

    if n <= 2:
        return n
    else:
        cache[0] = 1
        cache[1] = 2
        for i in range(2,n):
            cache[i] = cache[i-1] + cache[i-2]
            
    return cache[i]

#Testing code
print(climbStairs(5))
