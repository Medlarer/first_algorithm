import time
def cal_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        exp_time= time.time()-start
        print(exp_time)
    return inner


@cal_time
def bubble_sort(li):
    for i in range(len(li)-1):
        change = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j+1],li[j] = li[j],li[j+1]
                change = True
        if not change:
            return None




import random
li = list(range(1000))
random.shuffle(li)
print(li)
bubble_sort(li)
print(li)