import pdb

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])
        row_index=[]
        col_index=[]                    
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    row_index.append(i)
                    col_index.append(j)

        for i in row_index:
            matrix[i]=[0]*cols

        for j in col_index:
            for k in range(rows):
                matrix[k][j]=0


s = Solution()
matrix=[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
s.setZeroes(matrix)
print(matrix)     