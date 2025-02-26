class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        while matrix:
            res += matrix.pop(0) #[1,2,3,4]

            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop()) #[4,8,12]

            if matrix:
                res += matrix.pop()[::-1] #[12,11,10,9]

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0)) #[9,5,1]

        return res
