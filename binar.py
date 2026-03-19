import time, random

def timer(func):
    def wrapper(*args, **kwargs): 
        start = time.time()
        result = func(*args, **kwargs)  
        end = time.time()  
        print(f"Функция {func.__name__} выполнилась за {end - start:.6f} сек")
        return result
    return wrapper

@timer
def nsearch(a, find):
    for el in a:
        if find == el:
            return a.index(el)

@timer
def search(a, find):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if find == a[mid]:
            return mid 
        elif a[mid] > find:
            right = mid - 1
        else:
            left = mid + 1
    return None


a = [x for x in range(10000)] 
#print(a)
find = 999
print(find)
print(search(a, find))
print(nsearch(a, find))