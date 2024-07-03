#напишите программу ,которая будет выдавать день недели по введенному числу
a=input("ввидите день недели: ")
day=int(a)
if day==1:
    print("понедельник")
if day==2:
    print("вт")
if day==3:
    print("ср")
if day==4:
    print("чт")
if day==5:
    print("пт")
if day==6:
    print("сб")
if day==7:
    print("вск")
# if day>7:
#     print("это не день недели")
# if day<1:
#     print("это не день недели")


if day>7 or day<1:
    print("это не день недели")

