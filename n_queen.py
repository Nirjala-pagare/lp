
def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()


def solve_nqueens(row, n, board, columns, left_diagonal, right_diagonal):

    if row == n:
        print("Solution:")
        print_board(board, n)
        return True

    found_solution = False

    for col in range(n):

       
        if columns[col] == False and left_diagonal[row + col] == False and right_diagonal[row - col + n - 1] == False:

            
            board[row][col] = 1
            columns[col] = True
            left_diagonal[row + col] = True
            right_diagonal[row - col + n - 1] = True

            found_solution = solve_nqueens(row + 1, n, board, columns, left_diagonal, right_diagonal) or found_solution

            board[row][col] = 0
            columns[col] = False
            left_diagonal[row + col] = False
            right_diagonal[row - col + n - 1] = False

    return found_solution



n = int(input("Enter number of queens: "))

board = [[0 for _ in range(n)] for _ in range(n)]

columns = [False] * n
left_diagonal = [False] * (2 * n - 1)
right_diagonal = [False] * (2 * n - 1)

if not solve_nqueens(0, n, board, columns, left_diagonal, right_diagonal):
    print("No solution exists.")