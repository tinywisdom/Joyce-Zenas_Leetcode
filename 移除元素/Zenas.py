class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        head = 0
        tail = len(nums) - 1
        while  head < len(nums) and tail >= 0 and head <= tail:
            while head < len(nums) and nums[head] != val:
                head = head + 1
            while tail >=0 and nums[tail] == val:
                tail = tail - 1
            
            print(str(head) + "----" + str(tail))
            if head <= tail and head < len(nums) and tail >=0:
                nums[head] = nums[tail]
                nums[tail] = val
        
        return head