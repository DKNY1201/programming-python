def max_heapify(nums, i):
    l = 2 * i
    r = 2 * i + 1

    # we are using 1 index so need to reduce 1 to get correct value
    i -= 1
    l -= 1
    r -= 1
    lg = i

    if l < len(nums) and nums[l] > nums[i]:
        lg = l
    if r < len(nums) and nums[r] > nums[i]:
        lg = r

    if lg != i:
        nums[i], nums[lg] = nums[lg], nums[i]
        # +1 for 1 index
        max_heapify(nums, lg + 1)


def build_max_heap(nums):
    for i in range(len(nums) // 2, 0, -1):
        max_heapify(nums, i)


nums = [6, 4, 10, 2, 1, 7, 5]
build_max_heap(nums)
print(nums)

nums1 = [32, 100, 76, 45, 389, 10, 6, 14, 2, 9, 0, 1, 5, 4]
build_max_heap(nums1)
print(nums1)
