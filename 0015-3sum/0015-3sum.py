def twoSum(arr,target):
    l=0
    r=len(arr)-1
    ans=[]
    while(l<r):
        if arr[l]+arr[r]==target:
            ans.append([-1*target,arr[l],arr[r]])
            l+=1
            r-=1
            while(l<r and arr[l]==arr[l+1]):
                l+=1
            while(l<r and arr[r]==arr[r-1]):
                r-=1
        elif arr[l]+arr[r]<target:
            l+=1
        else :
            r-=1
    return ans
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return triplets
        