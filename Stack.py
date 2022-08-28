#Stack implementation using LIST

stack = []
def push(num):
    stack.append(num)
    print("Pushed number is: ",num)
    print(stack[::-1])

def pop():
    if(len(stack) == 0):
        print("stack is empty")
    else:
        n=stack.pop()
        print("Popped number is: ",n)
        print(stack[::-1])

def display():
    if(len(stack) == 0):
        print("Stack is empty\n")
    else:
        print("Current stack elements are :\n",stack[::-1])

while True:
    print("1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = int(input("Enter a choice\n"))
    if(choice==1):
        num = int(input("Enter a number to push\n"))
        push(num)
    elif(choice==2):
        pop()
    elif(choice==3):
        display()
    else:
        exit(0)

#Code by Shrikant
