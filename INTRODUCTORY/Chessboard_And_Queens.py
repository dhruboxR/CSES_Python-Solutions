chessBoard = [ list(input().strip()) for _ in range(8) ]        # Read the Chess Board [ list of list ]
totalPlacements = 0

def is_Safe(r, c) :
    # CHECK FOR QUEENS IN THE SAME COLUMN
    for i in range(r) :
        if chessBoard[ i ][ c ] == 'Q' : return False
    
    # CHECK FOR QUEENS IN THE UPPER-LEFT DIAGONAL
    i, j = r-1, c-1
    while i >= 0 and j >= 0 :
        if chessBoard[ i ][ j ] == 'Q' : return False
        i -= 1
        j -= 1
    
    # CHECK FOR QUEENS IN THE UPPER-RIGHT DIAGONAL 
    i, j = r-1, c+1
    while i >= 0 and j < 8 :
        if chessBoard[ i ][ j ] == 'Q' : return False
        i -= 1
        j += 1
    
    return True

def count_Placements(row) :
    global totalPlacements

    # All 8 Queens are placed in the chessBoard
    if row == 8 :
        totalPlacements += 1
        return
    
    # For each column how many ways are there to put a queen 
    for col in range(8) :
        if chessBoard[ row ][ col ] == '*' : continue   # BLOCKED CELL

        if is_Safe(row, col) :
            chessBoard[ row ][ col ] = 'Q'      # PLACE A QUEEN HERE 

            count_Placements(row + 1)         # Try placing Queen in the next row

            chessBoard[ row ][ col ] = '.'      # Undo choice and try other options [ backtrack ]

# start by placing queen from the first row 
count_Placements(0)

print( totalPlacements )
