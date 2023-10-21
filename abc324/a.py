N = int(input())
nums = list(map(int, input().split()))

print("Yes" if nums.count(nums[0]) == N else "No")
