def findMedianSortedArrays(nums1, nums2) -> float:
    merged_list = []
    for num in nums1:
        merged_list.append(num)
    for num in nums2:
        merged_list.append(num)
    sorted_list = sorted(merged_list)
    if len(merged_list) % 2 != 0:
        median = sorted_list[(len(sorted_list) - (len(sorted_list) // 2)-1)]
    else:
        median = (sorted_list[len(sorted_list) // 2] + sorted_list[(len(sorted_list) // 2) - 1]) / 2

    return float(median)


print(findMedianSortedArrays([1,3],[2]))