def isValidSudoku(board) -> bool:
    # This funciton will check for conflictions in a list
    def isValid(l) -> bool:
        return len(l)-l.count('.')+1 == len(set(l))
    for row in board:
        if not isValid(row):
            return False

    for columnIndex in range(9):
        if not isValid([row[columnIndex] for row in board]):
            return False

    for rowIndex in range(0,9,3):
        for columnIndex in range(0,9,3):
            if not [cell for cells in [row[columnIndex:columnIndex+3] for row in board[rowIndex:rowIndex+3]] for cell in cells]:
                return False
    return True





def main():
    test1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    test2 = [["8","3",".",".","7",".",".",".","."] ,["6",".",".","1","9","5",".",".","."] ,[".","9","8",".",".",".",".","6","."] ,["8",".",".",".","6",".",".",".","3"] ,["4",".",".","8",".","3",".",".","1"] ,["7",".",".",".","2",".",".",".","6"] ,[".","6",".",".",".",".","2","8","."] ,[".",".",".","4","1","9",".",".","5"] ,[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(test1))
    print(isValidSudoku(test2))

    
if __name__ == "__main__":
    main()
