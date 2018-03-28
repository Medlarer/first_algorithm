
def bubble_sort(li):
    for i in range(len(li)-1):
        change = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                change = True
            if not change:
                return None