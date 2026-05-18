class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2D binary search

        low_r, high_r = 0, len(matrix)-1
        low_c, high_c = 0, len(matrix[0])-1
        mid_r, mid_c = -1, -1
        row_yes = False

        while low_r <= high_r:
            mid_r = (low_r + high_r) // 2
            if matrix[mid_r][low_c] <= target and matrix[mid_r][high_c] >= target:
                row_yes = True
                break
            elif matrix[mid_r][high_c] < target:
                low_r = mid_r + 1
            else:
                high_r = mid_r - 1

        if not row_yes:
            return False

        while low_c <= high_c:
            mid_c = (low_c + high_c) // 2
            if matrix[mid_r][mid_c] == target:
                return True
            elif matrix[mid_r][mid_c] < target:
                low_c = mid_c + 1
            else:
                high_c = mid_c - 1

        return False