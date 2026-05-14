class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Initialize lists of sets to track seen numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # Identify which 3x3 box we are in (index 0-8)
                # Formula: (row_index // 3) * 3 + (col_index // 3)
                box_idx = (r // 3) * 3 + (c // 3)

                # Check if value already exists in this row, col, or box
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_idx]):
                    return False
                
                # Add value to the sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True