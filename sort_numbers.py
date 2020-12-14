# quick sort
def solution(nums):
    if nums:
        return solution([*filter(lambda x: x <= nums[0], nums[1:])]) + [nums[0]] + solution([*filter(lambda x: x > nums[0], nums[1:])])
    return []
