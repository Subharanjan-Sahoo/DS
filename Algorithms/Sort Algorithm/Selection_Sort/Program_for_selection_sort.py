list = [5,15,3,12,17,0]
print("Unsorted",list) # list

for i in range(len(list)-1):
    min_val = list[i]
    for j in range(i+1,len(list)):
        if list[j] < min_val:
            min_val = list[j]

    min_ind =list.index(min_val,i) # We have to put i then the no duplicate value program
    if list[i] != list[min_ind]:
        list[i],list[min_ind] =list[min_ind],list[i]
    print(list)
print("sorted",list)    