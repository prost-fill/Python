def sum(list):
    if list == []:
        return 0
    return list[0]+sum(list[1:]) 

def qsort(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x<=pivot]
        bigger = [x for x in array[1:] if x>pivot]
    return qsort(less) + [pivot] + qsort(bigger)

def counter(list):
    if list == []:
        return 0
    return 1+counter(list[1:])

def maximum(list):
    if len(list) == 2:
        return list[0] if  list[1]<list[0] else list[1]
    max = maximum(list[1:])
    return list[0] if list[0]> max else max

    

array=[22,15,24,17,33,23,22,16]

print(array)
print(sum(array))
print(counter(array))
print(maximum(array))
print(qsort(array))

