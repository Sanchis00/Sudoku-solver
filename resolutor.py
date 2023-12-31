

N = 9

def isSafe(sudoku,row,col,num):
    for i in range(9):
        if sudoku[row][i] == num:
            return False
    
    for i in range(9):
        if sudoku[i][col] == num:
            return False
        

    startRow = row - row % 3
    startColumn = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[startRow + i][startColumn+j] == num:
                return False
            
    return True

def resolutorSudoku(sudoku,row,col):
    if row==N -1 and col == N:
        return True
    
    if col == N:
        row+=1
        col=0

    if sudoku[row][col] > 0:
        return resolutorSudoku(sudoku,row,col+1)

    for num in range(1,N + 1):
        if isSafe(sudoku,row,col,num):
            sudoku[row][col]=num

            if resolutorSudoku(sudoku,row,col+1):
                return True
            
        sudoku[row][col] = 0
        
    return False

def solver(sudoku):
    if resolutorSudoku(sudoku,0,0):
        return sudoku
    else:
        return "No"