
def two_sum_sorted(nums, target):
    """Find two indices whose values sum to target.

    Unlike C++, Python lists can be accessed and updated without
    declaring an explicit vector type.
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]


if __name__ == "__main__":
    nums = [1, 2, 4, 6, 10]
    target = 8
    print(two_sum_sorted(nums, target))
