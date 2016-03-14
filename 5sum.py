"""
give all tuple (a,b,c,d,e) in non-descending order which make n[a]+n[b]+n[c]+n[d]+n[e]=target
the solution set must not contain duplicate tuples

"""
class Solution(object):
    def fiveSum(self, nums, target):
        nums.sort()
        rst = []
        for n in range(len(nums)-4):
            if n > 0 and nums[n-1] == nums[n]:
                continue
            for m in range(n+1, len(nums)-3):
                if nums[m-1] == nums[m] and m-n > 1:  ### m-n >1 is important (test [-4,-3,-3,-2,-1,0,1,2,5,7])
                    continue
                for i in range(m+1, len(nums)-2):
                    if nums[i-1] == nums[i] and i-m > 1: ### i-m >1 is important
                        continue
                    j, k = i+1, len(nums)-1
                    while j < k :
                        if nums[j] + nums[k] < target-nums[i]-nums[m]-nums[n]:
                            j += 1
                        elif nums[j] + nums[k] > target-nums[i]-nums[m]-nums[n]:
                            k -= 1
                        else:
                            rst.append([nums[n], nums[m], nums[i], nums[j], nums[k]])
                            j += 1
                            k -= 1
                            while j < k and nums[j] == nums[j-1]:
                                j += 1
                            while j < k and nums[k] == nums[k+1]:
                                k -= 1
        return rst

