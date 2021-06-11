list = [10,15,4,23,0]
print("Unsotted", list)
for j in range(len(list)-1):
    for i in range(len(list)-1):
        if list[i] > list [i+1]:
            list[i] ,list[i+1] =list[i+1],list[i]
            print('Itearations',list)
        else:
             print(list)
        print()     
print('sorted',list)            
