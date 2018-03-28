#一趟遍记录最小的数，放到第一个位置
#再一趟遍历剩余列表中最小数的位置。
import time
def cal_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        exp_time= time.time()-start
        print(exp_time)
    return inner

@cal_time
def select_sort(li):
    for i in range(len(li)-1):
        # i 表示趟数，也表示无序区开始的位置
        min_loc = i #最小数的位置
        for j in range(i+1,len(li)-1):
            if li[j] < li[min_loc]:
                min_loc = j
        if i != min_loc:
            li[i],li[min_loc] = li[min_loc],li[i]
            

import random
li = list(range(2000))
random.shuffle(li)
print(li)
print(select_sort(li))
print(li)
