from collections import defaultdict
import pdb
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def place_num(d,row,col):
            rows[row][d]+=1
            cols[col][d]+=1
            boxes[box_index(row,col)][d]+=1

        def could_place(d,row,col):
            return not (rows[row][d] or cols[row][d] or boxes[box_index(row,col)][d])

        def place_next_num(row,col):
            if row == 8 and col == 8:
                isSudo = True
            else:
                if col == 8:
                    backtrack(row+1,col)
                else:
                    backtrack(row,col+1)
            return

        def remove_num(d,row,col):
            rows[row][d]-=1
            cols[col][d]-=1
            boxes[box_index(row,col)][d]-=1


        def backtrack(row=0,col=0):
            if board[row][col]=='.':
                for d in range(9):
                    if could_place(d,row,col):
                        place_num(d,row,col)
                        place_next_num(row,col)
                        if not isSudo:
                            remove_num(d,row,col)
            else:
                place_next_num(row,col)

        rows = [defaultdict(int) for i in range(9)]
        cols = [defaultdict(int) for i in range(9)]
        boxes = [defaultdict(int) for i in range(9)]
        box_index = lambda row,col:row//3*3+col//3
        isSudo = False
            
        #intial record dic
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    d = int(board[i][j])
                    place_num(d,i,j)
                
        backtrack()
     



s = Solution()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)
print(board)