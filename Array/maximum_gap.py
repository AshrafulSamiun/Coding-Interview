
def maximum_gap(nums):
    nums.sort()
    n=len(nums)

    if n==1:
        return 0
    max_diff=0
    for i in range(1,n):
        diff=nums[i]-nums[i-1]
        if(diff>max_diff):
            max_diff=diff
    return max_diff

list=[3,6,9,1]
result=maximum_gap(list)
print(result)


