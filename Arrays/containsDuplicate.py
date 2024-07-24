class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Checks if a list contains any duplicates.
        
        This method iterates through the list of integers and uses a set to track the elements 
        that have been seen so far. If an element is found that is already in the set, it returns True, 
        indicating that there is a duplicate. If no duplicates are found by the end of the iteration, 
        it returns False.
        
        Parameters:
        nums (list[int]): A list of integers to check for duplicates.
        
        Returns:
        bool: True if there is at least one duplicate element, False otherwise.
        
        Example:
        >>> Solution().containsDuplicate([1, 2, 3, 4])
        False
        >>> Solution().containsDuplicate([1, 2, 3, 1])
        True
        
        Time Complexity: O(n) - Each element is checked once and the set operations (add and check membership) 
                         are on average O(1).
        Space Complexity: O(n) - In the worst case, all elements are unique and stored in the set.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False