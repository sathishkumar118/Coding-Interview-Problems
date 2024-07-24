class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Finds the minimum element in a rotated sorted array.
        
        The array is initially sorted in ascending order but then rotated at some unknown pivot. 
        This method uses an iterative binary search approach to find the minimum element efficiently.
        
        Parameters:
        nums (List[int]): A list of integers representing the rotated sorted array.
        
        Returns:
        int: The minimum element in the array.
        
        Example:
        >>> Solution().findMin([4, 5, 6, 7, 0, 1, 2])
        0
        
        Time Complexity: O(log n) - The binary search reduces the problem size by half each step.
        Space Complexity: O(1) - No additional space is used apart from variables.
        """
        left, right = 0, len(nums) - 1
        
        # If the array is not rotated (the smallest element is the first element)
        if nums[left] <= nums[right]:
            return nums[left]
        
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is greater than the rightmost element,
            # the minimum is in the right part
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        # The left pointer will be pointing to the minimum element
        return nums[left]