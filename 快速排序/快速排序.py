#归为
#递归
import time
import random,copy
def cal_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        exp_time= time.time()-start
        print(exp_time)
    return inner

# from .import cal_time
def partition(li,left,right):
    usu = random.randint(left+1,right)
    left,usu = usu,left
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left

@cal_time
def quick_sort(li):
    return _quick_sort(li,0,len(li)-1)

def _quick_sort(data,left,right):
    if left < right:
        mid = partition(data,left,right)
        _quick_sort(data,left,mid-1)
        _quick_sort(data,mid+1,right)
@cal_time
def sys_sort(li):
    li.sort()

li= [i for i in range(10000)]
random.shuffle(li)
li1= copy.deepcopy(li)
li1.reverse()
li2 = copy.deepcopy(li)
print(quick_sort(li1))
print(sys_sort(li2))
print(li)
