import time
def cal_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        exp_time= time.time()-start
        print(exp_time)
    return inner
# def a():
#     print( 'hello')
# a=cal_time(a)
# a()

# for i in range(100,-1,-1):
#     print(i)