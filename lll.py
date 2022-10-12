'''
a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
if a > b:
    print ("Первое число больше")
elif b > a:
    print ("Второе число больше")
    
    





a = int(input("Cоздайте пароль"))
b = int(input("Подтвердите пароль"))
if a == b:
    print("Пароль подтверждён")
else:
    print("Пароль неверный")








import keyboard

while True:
    if keyboard.is_pressed('0') == True:
        print("Ыыы")
        break1
    if keyboard.is_pressed('1') == True:
        print("Макака")
        break
    if keyboard.is_pressed('2') == True:
        print("Ууу")
        break
    if keyboard.is_pressed('3') == True:
        print("Чоо")
        break
    if keyboard.is_pressed('4') == True:
        print("Ок")
        break
    if keyboard.is_pressed('5') == True:
        print("Эм ок99")
        break
    if keyboard.is_pressed('6') == True:
        print("Эм")
        break
    if keyboard.is_pressed('7') == True:
        print("Хорощоу")
        break
    if keyboard.is_pressed('8') == True:
        print("Эээ")
        break
    if keyboard.is_pressed('9') == True:
        print("Чо надо")
        break






a = int(input("Введите любое число"))
if a % 2 == 0:
    int(input("Число четное"))
else:
    int(input("Число нечетное"))





a = int(input("Введите любое число ыыы"))
if a % 3 == 0:
    print("Число делится на три")
else:
    print("Число не делится на три")

if a > 0:
    print("Число больше нуля")
else:
    print("Число меньше нуля!!!!!!!!!!!!!!!!!!!!!!!!!")

'''



x = int(input("Введите сумму покупки"))
proc = x * 0.3
skid = x - proc
if x > 1000:
    print("С учётом скидки ", skid)
else:
    print("Эм вы не набрали до скидки, поэтому сумма покупки будет равна", x)




















