K = int(input().strip()) - 1
three_two_one_nums = [str(i) for i in range(1, 10)]

i = 0
while len(three_two_one_nums) <= K:
    for v in range(10):
        # 新しい桁が前の桁より小さいことを確認
        if v < int(three_two_one_nums[i][-1]):
            three_two_one_nums.append(three_two_one_nums[i] + str(v))
    i += 1

print(three_two_one_nums[K])
