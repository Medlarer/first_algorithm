def select_sort(li):
    for i in range(len(li)):
        min_loc = i #无序区的第一个数
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if i != min_loc:
            li[i],li[min_loc] = li[min_loc],li[i]

import random
li = list(range(100))
random.shuffle(li)
print(li)
print(select_sort(li))
print(li)
