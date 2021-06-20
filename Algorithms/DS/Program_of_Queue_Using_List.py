# First Program

queue = []
queue.append(10)
queue.append(20)
print(queue)  #print the queue
queue.append(30)
print(queue)  #print the queue
queue.pop(0)
print(queue)  #print the queue
queue.pop(0)
print(queue)  #print the queue
queue.pop(0)
print(queue)  #print the queue

print()
print("------------------------------")
print()
# Second Program

queue = []
queue.insert(0,10)
queue.insert(0,20)
print(queue)
queue.insert(0,30)
print(queue)
queue.pop()
print(queue)
queue.pop()
print(queue)
queue.pop()
print(queue)

# Full Program

queue= []
def enqueue():
    num = int(input("Enter the element: "))
    queue.append(num)
    print(num,"is added to queue! ")
def dequeue():
    if not queue:
        print("queue is empty!") 
    else:
        e = queue.pop(0)
        print("Removed element: ",e)
def display():
    print(queue)               



while True:
    print("Select the operation 1.add 2.remove 3.show 4.quit")
    choose = int(input("Enter the the Choose: "))
    if choose == 1:
        enqueue()
    elif choose == 2:
        dequeue()
    elif choose == 3:
        display()
    elif choose == 4:
        break
    else:
        print("Enter the correct operation!")       
