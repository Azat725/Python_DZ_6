while True:
    try:
        start = input('Чтобы НАЧАТЬ напишите "Start", чтобы ВЫЙТИ напишите "Exit"')
        if start.lower() == 'Exit':
            break
        if start == 'Start':
            num1 = int(input('Введите первое число: '))
            num2 = int(input('Введите второе число: '))
            operation = input('Выберите операцию:\n "+"\n "-"\n "*"\n "/"\n')
            
            if operation == '+':
                summary = num1 + num2
                print(f'{num1} + {num2} = {summary}')
            elif operation == '-':
                sub = num1 - num2
                print(f'{num1} - {num2} = {sub}')
            elif operation == '*':
                app = num1 * num2
                print(f'{num1} * {num2} = {app}')
            elif operation == '/':
                div = num1 + num2
                print(f'{num1} / {num2} = {div}')
            else:
                print('Неверная операция!')
                continue
            
    except ValueError:
        print('Введены неверные данные!')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')