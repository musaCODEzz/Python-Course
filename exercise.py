def contains_dups(nums):
    return len(nums) != len(set(nums))

user_input = input('Enter your numbers and space them')
nums = [int(x) for x in user_input.split()]

results = contains_dups(nums)
print(results)