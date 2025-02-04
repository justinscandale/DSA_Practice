#  LINK TO PROBLEM:
#  https://leetcode.com/problems/search-a-2d-matrix/description/

#  TAGS:
#  BIANRY SEARCH

#  SOLUTION:
#  Because every row is sorted in the 2d array
#  and the min element in row i+1 will always be >= the last element in row i
#  We know we can use a binary search on this array to find the solution
#  We can implement a 2d binary search where we first find the row
#  then find the index within that row 

# TIME COMPLEXITY:  O(logn)
# SPACE COMPLEXITY:  O(1)

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
   
    ROWS, COLS = len(matrix), len(matrix[0])
    top, bottom = 0, ROWS-1

    #find row to search
    while top <= bottom:
        row = (top+bottom)//2
        
        if target > matrix[row][-1]:
            top = row+1
        elif target < matrix[row][0]:
            bottom = row-1
        else:
            break
    
    #check if row valid
    if top>bottom:
        return False

    row = (top+bottom)//2
    left, right = 0, COLS-1

    #find elem in row
    while left <= right:
        mid = (left+right)//2

        if matrix[row][mid] > target:
            right = mid-1
        elif matrix[row][mid] < target:
            left = mid+1
        else:
            return True
        
    return False

#testing code
print( searchMatrix([[1,2,3],[4,5,6],[7,8,9]], 2) )