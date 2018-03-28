
def binary_search(li,val):
    low = 0
    high = len(li) - 1
    while low <= high :
        mid = (low + high) // 2
        if li[mid] > val:
            high = mid -1
        elif li[mid] < val:
            low = mid +1
        else:
            return mid
    else:
        return -1