def incrementer(nums, pos=1):
    return [(nums[0]+pos)%10] + incrementer(nums[1:], pos+1) if nums else []
