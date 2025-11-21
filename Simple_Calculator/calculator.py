def add(x,y):
    print("Result: ",(x+y))

def sub(x,y):
    print("Result: ",(x-y))
    
def mul(x,y):
    print("Result: ",(x*y))

def div(x,y):
    if y==0:
      print("Divide by 0 is not possible") 
    else:
      print("Result: ",(x/y))
      
print("SIMPLE CALCULATOR")
print("-----------------------------")
print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division")

ch=input("Enter choice(1/2/3/4):- ")

num1=float(input("Enter 1st no.:"))
num2=float(input("Enter 2nd no.:"))

if ch=='1':
    add(num1,num2)
elif ch=='2':
    sub(num1,num2)
elif ch=='3':
    mul(num1,num2)
elif ch=='4':
    div(num1,num2)
else:
    print("Invalid Choice")