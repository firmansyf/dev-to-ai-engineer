# nums = [1, 2, 3, 4, 5, 6]
# evens = []
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         evens.append(nums[i] * 10)

# f = open("log.txt")
# lines = f.readlines()
# f.close()



# iterasi ( enumerate, zip, reversed, .items() )

for name, item in enumerate(["Alice", "Bob", "Charlie"]):
    print(f"{item}: {name}")


print("=================================================")

d = {"a": 1, "b": 2, "c": 3}

for key, value in d.items():
    print(f"{key}: {value}")

print("=================================================")

# versi code menggunakan syntax idiom
nums = [1, 2, 3, 4, 5, 6]
evens = [n * 10 for n in nums if n % 2 == 0]

with open("log.txt") as f:
    lines = f.readlines()

print(evens)
print(lines)
