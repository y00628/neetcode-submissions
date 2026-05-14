class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        # horizontal right, vertical down (i, j+1) then (i+1, j)
        # num times - 1 for every other

        m, n = len(matrix), len(matrix[0])
        # seen = set() # for coords
        output = []

        top_pt, right_pt, bottom_pt, left_pt = 0, n-1, m-1, 0

        

        while len(output) < m*n:

            for i in range(top_pt, right_pt+1):
                if len(output) == m*n:
                    break
                # seen.add((top_pt, i))
                output.append(matrix[top_pt][i])

            top_pt += 1

            for i in range(top_pt, bottom_pt+1):
                if len(output) == m*n:
                    break
                # seen.add((i, right_pt))
                output.append(matrix[i][right_pt])

            right_pt -= 1

            for i in range(right_pt, left_pt-1, -1):
                if len(output) == m*n:
                    break
                # seen.add((bottom_pt, i))
                output.append(matrix[bottom_pt][i])

            bottom_pt -= 1

            for i in range(bottom_pt, top_pt-1, -1):
                if len(output) == m*n:
                    break
                # seen.add((i, left_pt))
                output.append(matrix[i][left_pt])

            left_pt += 1

        return output









        