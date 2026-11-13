class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):

            seen = set()

            for col in range(9):

                num = board[row][col]

                if num == ".":

                    continue

                if num in seen:
                    return False
                
                seen.add(num)
        
        for col in range(9):
            seen = set()

            for row in range(9):

                num = board[row][col]

                if num == ".":
                    continue

                if num in seen:
                    return False

                seen.add(num)

        for row_box in range(0, 9 , 3):
            for row_col in range(0, 9 , 3):

                seen = set()
                

                for row in range(row_box , row_box+3):
                    
                    for col in range(row_col , row_col + 3):

                        
                       
                        num = board[row][col]

                        if num == ".":
                            continue
                        if num in seen:
                            return False

                        seen.add(num)
                        
        return True

  




        