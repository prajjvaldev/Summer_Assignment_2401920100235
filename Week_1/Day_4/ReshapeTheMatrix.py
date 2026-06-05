class Solution:
    def matrixReshape(self, mat, r, c):

        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        flat = []

        for row in mat:
            flat.extend(row)

        result = []

        for i in range(0, len(flat), c):
            result.append(flat[i:i + c])

        return result
