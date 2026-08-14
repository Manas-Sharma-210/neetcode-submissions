class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for row in range(9):
            row_seen = set()
            for column in range(9):
                cell = board[row][column]
                if cell == ".":
                    continue
                elif cell in row_seen:
                    return False
                row_seen.add(cell)       

        for col in range(9):
            col_seen = set()
            
            for i in range(9):
                cell = board[i][col]
                if cell == ".":
                    continue
                if cell in col_seen:
                    return False
                col_seen.add(cell)

        for box in range(9):
            
            box_seen = set() 
            
            for i in range(3): 
                for j in range(3):
                    row = (box//3)*3+i
                    col = (box%3)*3+j
                    cell = board[row][col]
                    if cell == ".":
                       continue
                    if cell in box_seen:
                        return False
                    box_seen.add(cell)    

        return True                
        