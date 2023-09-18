degry=1
number= int(input("Введите число: "))
x=2
if(number>=x):
    while(x<=number):
        x=x*2
        degry=degry+1
    print(degry-1)
else:
    print("Введите число побольше")