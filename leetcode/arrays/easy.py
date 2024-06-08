# # Example 1:
# # Input: nums = [2,7,11,15], target = 9
# # Output: [0,1]
# # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# # Example 2:
# # Input: nums = [3,2,4], target = 6
# # Output: [1,2]
#
# # Example 3:
# # Input: nums = [3,3], target = 6
# # Output: [0,1]
#
#
# lst = [11, 15, 2, 7]
# lst = [3, 3]
# target = 9
# target = 6
# last_idx = len(lst) - 1
# first_idx = 0
# second_idx = 0
#
# def find_indices(nums, target):
#
#     last_idx = len(nums) - 1
#     first_idx = 0
#     second_idx = 0
#
#     while True:
#         print(f'first idx {first_idx}')
#         print(f'second_idx {second_idx}')
#
#         if second_idx == last_idx:
#             first_idx += 1
#             second_idx = first_idx
#             continue
#
#         tmp_sum = nums[first_idx] + nums[second_idx + 1]
#
#         if tmp_sum == target:
#             return [first_idx, second_idx + 1]
#
#         second_idx += 1
#
#
# find_indices(lst, target)
#
# nums = [11, 15, 2, 7]
# target = 9
#
# seen = {}
#
# for i in range(len(nums)):
#     diff = target - nums[i]
#     if diff in seen:
#         print(seen[diff], i)
#     else:
#         seen[nums[i]] = i
#
#
# x = 121
# x // 2
# x = -121
# x = 10

# remove duplicates in array
nums = [0, 0, 0, 1, 1, 2]
insert_idx = 1

for i in range(1, len(nums)):
    current = nums[i]
    prev = nums[i - 1]
    if current != prev:
        nums[insert_idx] = current
        insert_idx += 1

# max profit
prices = [1, 2, 7, 1, 5]

total = 0
for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        total += prices[i] - prices[i - 1]

# rotate array
nums = [1, 2, 3, 4, 5, 6, 7]
nums = [-1, -100, 3, 99]
nums = [1, 2]
k = 3
expected = [5, 6, 7, 1, 2, 3, 4]

while k:
    nums.insert(0, nums[-1])
    nums.pop(-1)
    k -= 1

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
nums = [1, 2, 3]


def check_duplicated(nums):
    seen = {}
    for n in nums:
        if n in seen.keys():
            return True
        else:
            seen[n] = True
    return False


# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
seen = {}
nums = [1, 2, 4, 1, 2]
for n in nums:
    if n not in seen:
        seen[n] = n
    else:
        seen.pop(n)

list(seen.keys())[0]

# WTF
a = 0
for i in nums:
    a ^= i

# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
from collections import defaultdict

nums1 = [1, 2, 2]
nums2 = [2, 2]

num1_dict = defaultdict(int)

# dict for num1
for num in nums1:
    if num in num1_dict:
        num1_dict[num] = num1_dict[num] + 1
    else:
        num1_dict[num] = 1

intersection = []
# iteration for num2
for num in nums2:
    if num in num1_dict and num1_dict[num] > 0:
        intersection.append(num)
        num1_dict[num] = num1_dict[num] - 1

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.
digits = [1, 2, 3]
digits = [4, 3, 2, 1]
digits = [9]
digits = [9, 2, 9]
digits = [3, 99]

[int(i) for i in str(int(''.join([str(i) for i in digits])) + 1)]

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

nums = [0, 1, 0, 3, 12]
nums = [0]
nums = [0, 0, 1, 0, 2]
nums = [0, 0, 1]

idx = 0
n = 0
while n != len(nums):
    if nums[idx] == 0:
        nums.pop(idx)
        nums.append(0)
        n += 1
    else:
        idx += 1
        n += 1

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

nums = [2,7,11,15]
target = 9

seen_dct = {}
for i in range(0, len(nums)):
    diff = target - nums[i]
    if i == 0:
        seen_dct[diff] = i
    elif nums[i] in seen_dct:
        print(f'[{seen_dct[nums[i]]}, {i}]')
    else:
        seen_dct[diff] = i

