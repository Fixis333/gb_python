numberOne=int((input("Введите сумму двух чисел: ")))
numberTwo=int((input("Введите произведение двух чисел: ")))
if numberOne<=1000 and numberTwo<=1000:
    x=0
    y=0
    while(x<numberTwo):
        while(y<numberTwo):
            if(x+y==numberOne and x*y==numberTwo):
                if x>y:
                    break
                print(x, y)
                break
            else:
                y=y+1
        y=0
        x=x+1