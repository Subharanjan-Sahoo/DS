Stack=[]
def push():
    element = input("Enter the element: ")
    Stack.append(element)
    print(Stack)

def pop_element():
    if not Stack:
        print("Stack is empty!")
    else:
        e = Stack.pop()
        print("Remove element: ",e)
        print(Stack)

while True:
    print("Select the operation 1. push  2. pop 3. quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        print (Stack)
        break
    else:
        print("Enter the correct operation!")
