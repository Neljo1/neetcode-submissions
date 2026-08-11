class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=nums.sort()
        c=0
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                c+=1
        if c>0:
            return True
        else :
            return False
            