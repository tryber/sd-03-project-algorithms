def find_duplicate(nums):
    """ Faça o código aqui. """
    if (not nums) or (len(nums) <= 1) or (type(nums[0]) == str):
        return False
    unique = list()
    dup = list()
    for i in range(len(nums)):
        if nums[i] not in unique:
            unique.append(nums[i])
        else:
            dup.append(nums[i])
    if len(dup) == 0:
        return False
    return int(dup[0])
