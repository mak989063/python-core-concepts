nums = []
def calc_product(nums):
    product = 1
    for i in range (len(nums)):
        product = product * nums[i]

    return product


print(calc_product([3,2,3,4]))