# nums = [1, 2, 3, 4, 5, 6]
# evens = []
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         evens.append(nums[i] * 10)

# f = open("log.txt")
# lines = f.readlines()
# f.close()


# versi code menggunakan syntax idiom
nums = [1, 2, 3, 4, 5, 6]
evens = [n * 10 for n in nums if n % 2 == 0]

with open("log.txt") as f:
    lines = f.readlines()

print(evens)
print(lines)
