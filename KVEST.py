from random import*
code = randint (1000,9999)
print ('Привет дорогой игрок, ты попал в мир постапокалипсиса, тебе нужно выжить и победить финального босса!') 
print('Введите ваше имя, а потом город, в котором вы живёте!')

name = str(input())
city = str(input())

print (f'Приветствуем тебя в мире постапокалипсиса, {name}!')
print (f"Вы проснулись по среди разрушенного города {city}, вам нужно выбрать действие ")

print ('1. Попробовать анализировать ситуацию и придумать план действий')
print ('2. Начать громко кричать')
print ('3. Продолжить спать')

choice = int(input())

if choice == 1:
    print ('Вы анализируете местности и делаете вывод, что вам нужно искать припасы и выживших, аккуратно пройдя мимо мутантов, вы заходите в торговый центр.')
elif choice == 2:
    print("После того, как вы закричали... Вы услышали множество громких звуков с разных сторон. Оглядевшись, вы увидели, что к вам на встречу бежит огромное количество мутантов. Вы встали, попробовали залезть на дерево стоящее рядом, но... Вас догнали и начали пожирать монстры.")
    print("Конец истории...Начните игру заново...")
    exit()
elif choice == 3:
    print ('Пока вы спали, вас съели...')
    print ('Конец истории...Начните игру заново...')
    exit()
else:
    print ('Вы опоздали... ОНО уже тут...')
    print ('Конец истории...Начните игру заново...')
    exit()

print ('Вы вошли в торговый центр, перед вами стоит сундук с замком... ')
print ('Чтобы сундук открылся, вам нужно ввести код:')
print ('Что бы получить код, вам нужно решить пример:')
print ('Реши пример: (7² - 3²) : 2 ')
otvet = int(input())
if otvet == 20:
    print (f'Вот ваш код: {code}!')
    print ('Введите код:')
    i = int(input())
    if i == code:
        print ('Сундук открылся, перед вами лежат 3 вещи: трусы, пистолет и носок')
        print ('Вам можно взять только один предмет.')
        print ('Что вы возьмете?')
        item = str(input())
        if item == 'носок' or item == 'трусы':
            print ('Эта вещь никак вам не помогла и вы погибли...')
            print ('Конец истории...')
            exit()
        elif item == 'пистолет':
            print ('Вы быстро схватили пистолет, через секунду услышали грохот СЗАДИ... У вас есть пара возможных действий:')
            print ('1. Начать бежать вперёд, перепрыгнув через сундук.')
            print ('2. Резко обернуться и увидеть источник звука.')
            print ('3. Лечь спать..')
            p = int(input())
            if p == 3 or p == 2 :
                print('Увы... ОНО напало на вас, не дав шанса выжить..')
                print('Конец истории...')
                exit
            elif p == 1:
                print ('Вы резко рванули вперед и перепрыгнули через сундук, резко развернувшись в прыжке вы увидели то самое ОНО, это был большой и мерзкий мутант.')
                print ('Вы нацелились ему в голову...')
                print ('1. Нажать на курок.')
                print ('2. Не нажимать на курок')
                print ('3. Обнять монстра')
                y = int(input())
                if y == 1:
                    print ('Вы cтрельнули в монстра. Звук выстрела услышали все монстры района, они уже идут за вами')
                    print ('Но оказалось, что рядом с вами ещё и военные, которые оказались недалеко от магазина, и они тоже идут к вам на помощь. ')
                    print ('Они отстрелились от всех мутантов и забрали вас на вертолёте. Вы улетели на базу и оказались спасены.')
                    print ('Хорошая концовка')
                    exit()
                elif y == 2 or y == 3:
                    print ('Вас съели...')
                    print ('Плохая концовка')
                    exit()
        else:
            print ('На сундуке сработала сигнализация, ОНО пришло к вам...')
            print ('Конец истории...')
            exit()
    else:
        print ('Вы ввели неправильный код и на сундуке сработала сигнализация, ОНО пришло к вам...')
        print ('Конец истории...')
        exit()
else:
    print('Получив неправильный код, вы пытались ввести его на замке и на сундуке сработала сигнализация, ОНО пришло к вам...')
    print('Конец истории...')
    exit()
