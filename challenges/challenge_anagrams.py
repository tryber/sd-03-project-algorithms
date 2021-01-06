def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    # Python program for implementation of MergeSort
    first = list(first_string)
    second = list(second_string)
    mergeSort(first)
    print(first)
    mergeSort(second)
    print(second)

    if second == first:
        return True
    else:
        return False


# Driver Code
if __name__ == "__main__":
    arr = list("zasdasd")

    is_anagram(list("arr"), list("rar"))

# This code is contributed by Mayank Khanna
