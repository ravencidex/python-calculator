while True:
    try:
        inpyt1 = input("Введите первое число (q - выход): ")
        if inpyt1.lower() == "q":
            print("Спасибо за использование!")
            break
        c1 = int(inpyt1)
        inpyt2 = input("Введите второе число (q - выход): ")
        if inpyt2.lower() == "q":
            print("Спасибо за использование!")
            break
        c2 = int(inpyt2)    
        op = input("Введите вариант оператора(/,-,*,+): ")
        if op == "+":
            print("Результат:", c1 + c2)
        elif op == "-":
            print("Результат:", c1 - c2)
        elif op == "*":
            print("Результат:", c1 * c2)
        elif op == "/":
            print("Результат:", c1 / c2)
        else:
            print("Вы ввели неверный оператор")    
    except ValueError:
        print("Вы ввели что-то не то")
          
        
    