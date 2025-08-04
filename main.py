import os
import csv
from datetime import datetime

#Очистка консоли для удобства использования
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Главное меню калькулятора бюджета
def main_menu():
    while True:
        clear()
        #Стартовое оповещение пользователя при запуске
        print('========================================================')
        print('        Добро пожаловать в калькулятор бюджета!')
        print('========================================================')
        print('Подсказка:\n Чтобы выбрать действие введите его номер,\n который указан Слева от действия')
        print('========================================================')
        print()
        print('Выберите действие:')
        print('1. Добавить доходы')
        print('2. Добавить расходы')
        print('3. Статистика')
        print('4. Выход')
        print()

        #Ввод пользователем числа(его выбора)
        user_choice = input('Введите ваш выбор: ')

        #Отслеживание выбора пользователя
        if user_choice == '1':
            add_income()
        elif user_choice == '2':
            add_expense()
        elif user_choice == '3':
            show_statistics()
        elif user_choice == '4':
            calculator_exit()
            break
        else:
            print()
            print('Некорректная команда! Попробуйте снова.')
            print()

#Добавление дохода
def add_income():
    clear()
    print()
    while True:
        income_type = input('Введите тип дохода (например: зарплата, премия): ').lower()
        if income_type.strip() != '' and income_type[0].isalpha():
            break
        else:
            print('Ошибка! Введите тип дохода.')
            print()

    while True:
        try:
            print()
            income_amount = float(input('Введите сумму дохода: '))

            if income_amount >= 0:
                save_transaction(income_type, 'Доход', income_amount)
                print('--------------')
                print('Доход успешно записан!\nПосмотреть доходы можно в статистике')
                print('--------------')
                break
            else:
                print('Сумма дохода должна быть больше либо равна нулю!')

        except ValueError:
            print('Ошибка! Сумма дохода должна быть числом!')
    question_for_user()

#Добавление расхода
def add_expense():
    clear()
    print()
    while True:
        expense_type = input('Введите тип расхода (например: ЖКХ, налог, покупка): ').lower()
        if expense_type.strip() != '' and expense_type[0].isalpha():
            break
        else:
            print('Ошибка! Введите тип расхода.')
            print()

    while True:
        try:
            print()
            expense_amount = float(input('Введите сумму расхода: '))

            if expense_amount >= 0:
                save_transaction(expense_type, 'Расход', expense_amount)
                print('--------------')
                print('Расход успешно записан!\nПосмотреть Расходы можно в статистике')
                print('--------------')
                break
            else:
                print('Сумма Расхода должна быть больше либо равна нулю!')

        except ValueError:
            print('Ошибка! Сумма расхода должна быть числом!')
    question_for_user()

#Отображение статистики
def show_statistics():
    clear()
    total_income = 0
    total_expense = 0
    print()
    print('========================================================')
    print('                Статистика транзакций')
    print('========================================================')
    try:
        with open('transactions.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            first_row = next(reader, None)
            # Проверяем, заголовок ли это (например, содержит "дата" или "тип")
            if first_row is not None and (
                'дата' in first_row[0].lower() or
                'тип' in first_row[1].lower() or
                'категория' in first_row[2].lower()
            ):
                # Это заголовок — пропускаем и дальше читаем
                pass
            else:
                # Это не заголовок — нужно обработать эту строку тоже
                if first_row is not None and len(first_row) == 4:
                    date, t_type, category, amount_str = first_row
                    try:
                        amount = float(amount_str)
                    except ValueError:
                        amount = 0
                    cat_clean = category.strip().lower()
                    if cat_clean == 'доход':
                        total_income += amount
                    elif cat_clean == 'расход':
                        total_expense += amount
                    print(f'{date} | {t_type:<15} | {category.strip():<7} | {amount:10.2f} руб.')
            # Читаем остальные строки
            for row in reader:
                if len(row) != 4:
                    continue
                date, t_type, category, amount_str = row
                try:
                    amount = float(amount_str)
                except ValueError:
                    continue
                cat_clean = category.strip().lower()
                if cat_clean == 'доход':
                    total_income += amount
                elif cat_clean == 'расход':
                    total_expense += amount
                print(f'{date} | {t_type:<15} | {category.strip():<7} | {amount:10.2f} руб.')
    except FileNotFoundError:
        print('Нет данных для отображения. Сначала добавьте доход или расход.')

    print('---------------------------------------------')
    print(f'Общий доход  : {total_income:10.2f} руб.')
    print(f'Общие расходы: {total_expense:10.2f} руб.')
    print(f'Баланс       : {(total_income - total_expense):10.2f} руб.')
    print('=============================================')
    question_for_user()

#Запись транзакции
def save_transaction(t_type, category, amount):
    date_now = datetime.now().strftime('%d-%m-%Y')
    with open('transactions.csv', mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date_now, t_type, category, amount])

#Вопрос пользователю о продолжении использования
def question_for_user():
    while True:
        print()
        print('Желаете продолжить использовать калькулятор бюджета?')
        answer = input('Введите "Да" или "Нет" чтобы продолжить: ').strip().lower()
        if answer == 'да':
            return  # вернётся в вызывающую точку (меню уже внутри)
        elif answer == 'нет':
            calculator_exit()
        else:
            print()
            print('ОШИБКА! Введите "Да" или "Нет" чтобы продолжить')

#Выход из программы
def calculator_exit():
    clear()
    print('========================================================')
    print('                  До новых встреч!')
    print('========================================================')
    exit()

#Запуск главного меню
if __name__ == '__main__':
    main_menu()