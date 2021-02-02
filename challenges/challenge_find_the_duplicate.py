def find_duplicate(nums):
    setOfNums = set()
    for n in nums:
        if n in setOfNums:
            return n
        else:
            setOfNums.add(n)      
    return False
