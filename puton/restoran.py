print('Добро пожаловать сеть ресторанов "Наш вкус"')
print('У нас есть 3 филиала с разными национальными кухнями:')
print('Филиал 1: Китайская кухня\nФилиал 2: Японская кухня\nФилиал 3: Русская кухня')

filialy = input('\nНапишите, какой филиал хотите посетить (филиал 1, филиал 2, филиал 3): ')
order_list = []
menu = {}
total_price = 0

if filialy == 'филиал 1':
    print('Режим работы от 8 до 22')
    print('Меню:')
    menu = {
        "Свинина в кисло-сладком соусе": 109,
        "Курица Гун Бао": 99,
        "Жареный рис": 7.99,
        "Весенние роллы (4 шт.)": 149,
        "Утка по-пекински": 299,
        "Кисло-острый суп": 99,
        "Лапша Чао Майн": 89,
        "Димсам (6 шт.)": 129,
        "Тофу Ма По": 149,
        "Говядина с брокколи": 119
    }
elif filialy == 'филиал 2':
    print('Режим работы от 24 до 6')
    print('Меню:')
    menu = {
        "Суши (6 шт.)": 150.00,
        "Рамен": 120.00,
        "Якитори (шашлычки)": 100.00,
        "Такояки (6 шт.)": 130.00,
        "Тяхан (жареный рис)": 140.00,
        "Темпура (ассорти)": 170.00,
        "Мисо-суп": 90.00,
        "Окономияки": 110.00,
        "Сашими (ассорти)": 200.00,
        "Моти (десерт)": 80.00
    }
elif filialy == 'филиал 3':
    print('Режим работы с понедельника по субботу')
    print('Меню:')
    menu = {
        "Борщ с пампушками": 120.00,
        "Пельмени": 140.00,
        "Окрошка": 90.00,
        "Блины с икрой": 180.00,
        "Винегрет": 100.00,
        "Щи с говядиной": 110.00,
        "Селедка под шубой": 150.00,
        "Голубцы": 130.00,
        "Картошка с грибами": 110.00,
        "Кисель 1 литр": 80.00
    }
else:
    print('Вы написали что-то неправильно')
    exit()

for dish, price in menu.items():
    print(f"{dish}: {price} руб.")

print('Что вы хотите заказать? Напишите "все", чтобы завершить заказ.')

def add_dish(order_list, menu):
    total_price = 0
    while True:
        new_dish = input("\nВведите название блюда: ")
        if new_dish.lower() == 'все':
            print(f"\nВаш заказ: {order_list}")
            print(f"Общая сумма: {total_price} руб.")
            break
        elif new_dish in menu:
            order_list.append(new_dish)
            total_price += menu[new_dish]
            print(f"Вы добавили {new_dish}. Цена: {menu[new_dish]} руб.")
        else:
            print("Такого блюда нет в меню. Попробуйте снова.")

    return order_list, total_price

add_dish(order_list, menu)







