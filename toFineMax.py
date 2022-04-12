def findMaximum(list):
    maximum = list[0]
    for x in list:
        if x > maximum:
            maximum = x
    print(maximum)



findMaximum([1,2,3,51,8,41])