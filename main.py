import sqlite3
import crud_dep
import crud_majors
import crud_stud
import create_tables

MIN_CHOICE=1
MAX_CHOICE=4
CRUD_STUD=1
CRUD_DEP=2
CRUD_MAJOR=3
EXIT=4

def main():
    create_tables.create_newtab()
    choice=0
    while choice!=EXIT:
        display_main_menu()  
        choice=get_main_menu()
        
        if choice == CRUD_STUD:
            crud_stud.make_CRUD_Stud()
        elif choice == CRUD_DEP:
            crud_dep.make_CRUD_Dep()
        elif choice == CRUD_MAJOR:
            crud_majors.make_CRUD_Majors()

def display_main_menu():
    print(f'\n----- Главное меню реляционной базы данных -----')
    print(f'1. Открыть меню для управления информации о студентах.')
    print(f'2. Открыть меню для управления информации о факультетах.')
    print(f'3. Открыть меню для управления информации о специальностях.')
    print(f'4. Выйти из программы.')

def get_main_menu():
    choice=int(input('Введите ваш вариант: '))
    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Допустимые варианты: {MIN_CHOICE} - {MAX_CHOICE}.')
        choice = int(input('Введите ваш вариант: '))
    return choice

if __name__=='__main__':
    main()

