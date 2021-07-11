def selectionsort(lst):
    print("basic selection sort algorithm")
    for i in range(0,len(lst)-1):
        minindex=i
        for j in range(i+1,len(lst)):
            if lst[j]<lst[i]:
                minindex=j
        if minindex!=i:
            lst[j],lst[i]=lst[i],lst[j]
    return lst
a=[3,7,8,99,10]
print(selectionsort(a))