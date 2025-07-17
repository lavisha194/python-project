
print("1-add")
print("2-subtract")
print("3 -multiply")
print("4-divide")
print("5-exponent")
option=int(input("choose an operation"))

if (option in[1,2,3,4,5]):
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))

    if(option==1):
        result=num1+num2
    elif(option==2):
        result=num1-num2
    elif(option==3):
        result=num1*num2
    elif(option==4):
        result=num1/num2
    elif(option==5):
        result=num1**num2

else:
    print("invalid operation entered")
print("the result of the operation is{}".format(result))