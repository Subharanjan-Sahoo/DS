def Shellsort(alist):
    gap = len(alist)//2
    while gap>0:
       for index in range (gap,len(list1)):
        current_element = alist[index]
        pos = index
        while pos >= gap and current_element<alist[pos-gap]:
            alist[pos] = alist[pos - gap]
            pos= pos - gap
        alist[pos] = current_element
    gap =gap // 2    

num = int(input("list length:"))
list1 = [int(input()) for i in range(num)]
Shellsort(list1)
print("sorted list:", list1)
