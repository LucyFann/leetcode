import pdb
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxs = [{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    num = int(board[i][j])
                    rows[i][num] = rows[i].get(num,0)+1
                    cols[j][num] = cols[j].get(num,0)+1
                    boxs[i//3*3+j//3][num] = boxs[i//3*3+j//3].get(num,0)+1
                    if rows[i][num]>1 or cols[j][num]>1 or boxs[i//3*3+j//3][num]>1:
                        return False
        return True

c = Solution()

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

print(c.isValidSudoku(board))