# напишите программу,которая на вход принимает 3 числа и выдает максимальное из них
a=input("ввидите первое число: ")
b=input("ввидите второе число: ")
с=input("ввидите третье число: ")
num1=int(a)
num2=int(b)
num3=int(с)
if num1>num2:
    if num1>num3:
        print("самое большое число первое",num1)
    else:
        print("самое большое число третье",num3)
else:
    if num2>num3:
        print("самое большое число второе",num2)
    else:
        print("самое большое число третье",num3)
print(max(num1,num2,num3))


