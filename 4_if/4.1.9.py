nums = list(map(int, input()))
print("ДА") if sum(nums[:3]) == sum(nums[3:]) else print("НЕТ")
