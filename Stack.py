#Stack implementation using LIST

stack = [1,2,3,4]
def push(num):
    stack.append(num)
    print("Pushed number is: ",num)
    print(stack)

def pop():
    n=stack.pop()
    print("Popped number is: ",n)
    print(stack)

def display():
    print("Current stack elements are :\n",stack)

def p(position,num):
    stack.insert(position,num)
    print("Updated stack: \n",stack)

while True:
    print("1. Push\n2. Pop\n3. Display\n4. Insert at specific position\n")
    choice = int(input("Enter a choice\n"))
    if(choice==1):
        num = int(input("Enter a number to push\n"))
        push(num)
    elif(choice==2):
        pop()
    elif(choice==3):
        display()
    elif(choice==4):
        position = int(input("Enter a position : "))
        num = int(input("Enter a number : "))
        p(position,num)
    else:
        exit(0)
