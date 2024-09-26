class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        def generate_row(row):
            ans = 1
            new_arr = []
            new_arr.append(1)
            for col in range(1,row):
                ans = ans * (row - col)
                ans = int(ans / col)
                new_arr.append(ans)

            return new_arr

        arr = []
        for i in range(1,numRows+1):
            temp = generate_row(i)
            arr.append(temp)

        return arr
            


        