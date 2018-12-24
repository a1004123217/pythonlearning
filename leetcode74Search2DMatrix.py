class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if (not matrix) or (target is None):
            return False
        r = len(matrix)
        c = len(matrix[0])

        low, high = 0, r * c - 1

        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // c][mid % c]

            if target == num:
                return True
            elif target < num:
                high = mid - 1
            else:
                low = mid + 1
        return False