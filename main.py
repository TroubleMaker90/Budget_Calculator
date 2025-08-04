def main_menu():
    print('========================================================')
    print('        Добро пожаловать в калькурятор бюджета!')
    print('========================================================')
    print('Подсказка:\n Чтобы выбрать действие введите его номер,\n который указан Слева от действия')
    print('========================================================')
    print()
    print('Выберите действие:')
    print('1. Добавить доходы')
    print('2. Добавить расходы')
    print('3. Статистика')
    print('4. Выход')

    user_choice = input()

    if user_choice == '1':
        add_income()
    elif user_choice == '2':
        add_expense()
    elif user_choice == '3':
        show_statistics()
    elif user_choice == '4':
        exit()

def add_income():
    pass

def add_expense():
    pass

def show_statistics():
    pass

def exit():
    pass

main_menu()