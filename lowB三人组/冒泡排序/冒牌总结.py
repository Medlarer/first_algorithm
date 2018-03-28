#冒泡排序的总次数是n-1次
import random
def bubble_sort(li):
    for i in range(len(li)-1):
    #i 表示次数
    # 第i趟时：无序区（0，len(i)-1）
        for j in range(0,len(li)-i-1):
            if li[j] > li[j+1]:
                li[j+1],li[j] = li[j],li[j+1]
li = list(range(1000))