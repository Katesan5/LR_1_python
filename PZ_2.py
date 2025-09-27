import copy
n_z = 1
while n_z != 0:
    n_z = int(input('\nВведи номер задания от 1 до 7, если захочешь выйти введи 0: '))
    if n_z == 1:
        a = int(input())
        b = float(input())
        print ('Сумма = ', a+b, ', разность = ', a-b, ' или ', b-a, ', произведение = ', a*b, ', результат от деления a/b = ', a/b)
        s = 3.14159*(5**2)
        print ('S = {:.2f}'.format(s))

    if n_z == 2:
        text = ' Hallo, Python! '
        text1 = text.strip()
        text2 = text1.replace('!', '?')
        text3 = text2.upper()
        print(text3)

    if n_z == 3:
        num = [7, 2, 5]
        num.append(4)
        num.insert(1, 10)
        num.extend([1, 1, 1])
        num.remove(7)
        num.pop()
        num.sort()
        num.reverse()
        print (num.count(2))
        print (num.index(1))
        num1 = num.copy()
        num2 = copy.deepcopy(num)
        num.clear()
        print (num)
        print (num1)
        print (num2)

    if n_z == 4:
        t = (1, 2, 3)
        t1 = (4, 5)
        t2 = t + t1
        print (t2)
        print (t2.count(3))
        print (t2.index(4))
        print (t)

    if n_z == 5:
        val = [3, 1, 3, 2, 1, 5, 2]
        un_val = set(val)
        print (un_val, 'Количество элементов - ', len(un_val))
        other = {2, 4, 5}
        print ('Пересечение: ', un_val&other, ', объединение: ', un_val|other)
        print ('Разности ', un_val-other, ' или ', other-un_val)

    if n_z == 6:
        scores = {"Alice": 85, "Bob": 90}
        scores["Charlie"] = 78
        scores["Bob"] = 95
        print (scores.get("Dave"))
        print (scores.get("Bob"))
        scores.pop("Alice")
        print (scores)
        print ('Ключи: ', scores.keys(), ', значения: ', scores.values())

    if n_z == 7:
        text = """
            Python is a powerful programming language. 
            It is used in data science, web development, automation, and many other fields!
            PYTHON is easy to learn, yet very versatile.
        """
        text1 = text.strip().lower().replace('!', '.')
        t1 = text1.split('.')
        t2 = [t1.strip() for t1 in t1 if t1.strip]
        print (t2)
        tt = t2[0]
        tt1 = tt.split()
        print (tt)





