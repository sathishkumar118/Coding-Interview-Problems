class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict = {}
        for i,n in enumerate(nums):
            new_tar = target - n
            if new_tar in mydict:
                return [mydict[new_tar], i]
            mydict[n] = i
