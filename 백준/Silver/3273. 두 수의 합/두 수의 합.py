def twoSum(nums: list[int], target: int) -> int:
    nums_map = {}
    cnt = 0

    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            cnt += 1

    return cnt // 2

n = int(input())
l = list(map(int, input().split()))
t = int(input())
print(twoSum(l, t))