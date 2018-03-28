"""
取一个元素P（第一个元素），使元素P归位
列表被P分成两部分，左边都比P小，右边都比P大；
递归完成排序
"""
import time
def cal_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        exp_time= time.time()-start
        print(exp_time)
    return inner
@cal_time
def quick_sort(li):
    return _quick_sort(li,0,len(li)-1)

def _quick_sort(li,left,right):
    mid = partition(li,left,right)
    if left < right:
        _quick_sort(li,left,mid-1)
        _quick_sort(li,mid+1,right)

def partition(data,left,right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]
    data[left] = tmp
    return left

import copy,random

li= [i for i in range(10000)]
random.shuffle(li)
li1= copy.deepcopy(li)
# li1.reverse()
li2 = copy.deepcopy(li)
quick_sort(li)
# print(sys_sort(li2))
print(li)