#  LINK TO PROBLEM:
# https://leetcode.com/problems/kth-largest-element-in-an-array/

#  TAGS:
#  HEAPS

#  SOLUTION:
#  We first make an empty heap and then iterate through nums
#  We push num onto the min heap and if the length of the heap is greater than k we pop the smallest element
#  This way we have a heap of size k with the kth largest element at the top of the heap

# TIME COMPLEXITY:  O(n*log(k)) - for each element in nums add it to heap if it is smaller than the largest element in the heap
# SPACE COMPLEXITY:  O(k) - to make heap of size k

import heapq

def kthlargest(nums: list[int], k: int) -> int:

    heap = []
    heapq.heapify(heap)

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]
        

#testing code
nums=[2,3,1,5,4,5,5,6,1,2,2,3,4,5,6,7,8,9,10]
k=1
print(kthlargest(nums,k))