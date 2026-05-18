def display_board(board) :
    for row in board :
        for cell in row:
            print(" Q " if cell else " . ", end=" ")
        print()
    print()

def solve(board, row, cols, leftDiagonal, rightDiagonal):
    # base condition
    n = len(board)
    if row == n:
        print("Solution Found")
        display_board(board)
        return True

    for col in range(n) :
        ld = (row - col) + (n-1)
        rd = (row + col) 

        # branch and bound pruning
        if(cols[col] or leftDiagonal[ld] or rightDiagonal[rd]):
            continue

        board[row][col] = 1
        cols[col] = True
        leftDiagonal[ld] = True
        rightDiagonal[rd] = True

        if solve(board, row+1, cols, leftDiagonal, rightDiagonal):
            return True
        board[row][col] = 0

        cols[col] = False
        leftDiagonal[ld] = False
        rightDiagonal[rd] = False

    return False


def main():
    n = int(input("Enter N: "))

    board = [[0] * n for i in range(n)]

    cols = [False] * n
    leftDiagonal = [False] * (2*n - 1)
    rightDiagonal = [False] * (2*n - 1)

    if not solve(board, 0, cols, leftDiagonal, rightDiagonal):
        print("No solution exists")

main()