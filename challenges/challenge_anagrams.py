def is_anagram(first_string, second_string):
    if first_string and second_string:
        return merge_sort(list(first_string)) == merge_sort(list(second_string))
    return False
    
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        half = len(arr)//2
        return merge(merge_sort(arr[:half]), merge_sort(arr[half:]))

# merges two sorted arrays
def merge(a, b):
    merged = list()
    while len(a) and len(b):
        highest = a
        if b[0] < a[0]:
            highest = b
        merged.append(highest.pop(0))
    last = (a or b)
    while last:
        merged.append(last.pop(0))
    return merged