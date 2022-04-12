def isSorted(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] > list[j]:
                return False
    return True


print(isSorted([1,2,3,4,7,6]))