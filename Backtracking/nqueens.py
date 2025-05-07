def totalNQueens(n):
    def backtrack(row, diagonals, anti_diagonals, cols):
        if row == n:
            return 1  # Found one valid solution

        solutions = 0
        for col in range(n):
            curr_diag = row - col
            curr_anti_diag = row + col

            # Check if the position is under attack
            if col in cols or curr_diag in diagonals or curr_anti_diag in anti_diagonals:
                continue

            # Mark the position as used
            cols.add(col)
            diagonals.add(curr_diag)
            anti_diagonals.add(curr_anti_diag)

            # Move to the next row
            solutions += backtrack(row + 1, diagonals, anti_diagonals, cols)

            # Backtrack: remove the queen and try next column
            cols.remove(col)
            diagonals.remove(curr_diag)
            anti_diagonals.remove(curr_anti_diag)

        return solutions

    return backtrack(0, set(), set(), set())

n=int(input("Enter the number of queens/rows: ").strip())
print(totalNQueens(n))  # Output: 2
