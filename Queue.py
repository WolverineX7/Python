#Queue implementation using LIST

queue = []
def push(num):
    queue.append(num)
    print("Pushed element is:",num)
    print(queue)

def pop():
    if(len(queue) == 0):
        print("Queue is empty")
    else:
        n = queue.pop(0)
        print("Popped element is:",n)
        print(queue)

def display():
    if(len(queue) == 0):
        print("Queue is empty")
    else:
        print("Queue elements are:\n",queue)

while True:
    print("1. Push\n2. Pop\n3. Display\n4. Exit\n")
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
