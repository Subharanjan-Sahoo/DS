list = [5,15,3,12,17,0]
print("Unsorted",list) # list

for i in range(len(list)):
    min_val = min(list[i:])
    min_ind =list.index(min_val,i) # We have to put i then the no duplicate value program
    list[i],list[min_ind] =list[min_ind],list[i]
    print(list)
print("sorted",list)    