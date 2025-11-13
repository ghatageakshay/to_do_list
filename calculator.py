print("-----Calcultor-----")

def additon(num1,num2):
    return num1+num2

def substraction(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
    if num2==0:
        return "Error:Division By Zero!"
    
    else:
        return num1/num2
    

n=int(input("num1:"))
m=int(input("num2:"))
print("1.Addition\n 2.Substraction\n 3.Multiplication\n 4.Division")
while True:
    Choice=int(input("Enter your choice:"))
    if Choice==1:
        print("result=",additon(n,m))

    elif Choice==2:
        print("result=",substraction(n,m))
    
    elif Choice==3:
        print("result",multiplication(n,m))

    elif Choice==4:
        print("result",division(n,m))

    elif Choice==0:
        print("Existing Calculator.!!")
        break

    else:
        print("Inavlid Choice. Try Again")