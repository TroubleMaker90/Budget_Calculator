import os
import csv
from datetime import datetime


#Очистка консоли для удобства использования !! пока не используется
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Главное меню калькулятора бюджета
def main_menu():
    while True:
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
    print()
    while True:
        income_type = input('Введите тип дохода (например: зарплата, премия): ')
        if income_type.isalpha():
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
    print()
    while True:
        expense_type = input('Введите тип расхода (например: ЖКХ, налог, покупка): ')
        if expense_type.isalpha():
            break
        else:
            print('Ошибка! Введите тип расхода.')
            print()

    while True:
        try:
            print()
            expense_amount = float(input('Введите сумму расхода: '))

            if expense_amount >= 0:
                save_transaction(expense_type, 'Доход', expense_amount)
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
    pass

#Запись транзакции
def save_transaction(t_type, category, amount):
    date_now = datetime.now().strftime('%dd-%mm-%yyyy')
    with open('transactions.csv', mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date_now, t_type, category, amount])
#НЕ ОСНОВНЫЕ ФУНКЦИИ

#Вопрос пользователю о продолжении использования
def question_for_user():
    while True:
        print()
        print('Желаете продолжить использовать калькулятор бюджета?')
        answer = input('Введите "Да" или "Нет" чтобы продолжить: ')
        answer = answer.lower()
        if answer == 'да':
            main_menu()
        elif answer == 'нет':
            calculator_exit()
            break
        else:
            print('')
            print('ОШИБКА! Введите "Да" или "Нет" чтобы продолжить')

#Выход из программы
def calculator_exit():
    print('========================================================')
    print('                  До новых встреч!')
    print('========================================================')
    exit()

#Запуск стартового меню
main_menu()