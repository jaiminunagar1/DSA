def setZeroes1(matrix:[list[list[int]]]) -> None:
    r = len(matrix)
    c = len(matrix[0])
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j] == 0:
                k = 0 
                while k<c:
                    if matrix[i][k] !=0:
                        matrix[i][k] = float("inf")
                    k+=1
                k = 0
                while k<r:
                    if matrix[k][j] !=0:
                        matrix[k][j] = float("inf")
                    k+=1
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0
            
# Just for read ability make the function that make the row and column to infinity (This as same as above)

def makeinf(matrix,row,column):
    r = len(matrix)
    c = len(matrix[0])
    for i in range(0,r):
        if matrix[i][column] != 0:
            matrix[i][column] =float("inf")
    for i in range(0,c):
        if matrix[row][i] != 0:
            matrix[row][i] = float("inf")

def setZeroes2(matrix:[list[list[int]]]) -> None:
    r = len(matrix)
    c = len(matrix[0])
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j] == 0:
                makeinf(matrix,i,j)
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0


# Optimal

def setZeros3(matrix)->None:
        r = len(matrix)
        c = len(matrix[0])
        row_track = [0]*r
        column_track = [0]*c
        for i in range(0,r):
            for j in range(0,c):
                if matrix[i][j] == 0:
                    row_track[i] = -1
                    column_track[j] = -1
        for i in range(0,r):
            for j in range(0,c):
                if row_track[i] == -1 or column_track[j] == -1:
                    matrix[i][j] = 0

if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

    print(f"2 {setZeroes2(matrix=matrix.copy())}")
    print(matrix)
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(f"3 {setZeros3(matrix=matrix.copy())}")
    print(matrix)



