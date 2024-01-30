import sqlite3

MIN_CHOICE=1
MAX_CHOICE=6
NEW_DEP=1
FIND_DEP=2
UPDATE_DEP=3
DELETE_DEP=4
SHOW_ALL_DEP=5
EXIT=6

def make_CRUD_Dep():
    choice_CRUD_Dep=0
    while choice_CRUD_Dep!=EXIT:
        display_menu_dep()  
        choice_CRUD_Dep=get_menu_dep()
        
        if choice_CRUD_Dep == NEW_DEP:
            new_dep()
        elif choice_CRUD_Dep == FIND_DEP:
            find_dep()
        elif choice_CRUD_Dep == UPDATE_DEP:
            update_dep()
        elif choice_CRUD_Dep == DELETE_DEP:
            delete_dep()
        elif choice_CRUD_Dep == SHOW_ALL_DEP:
            show_dep() 

def display_menu_dep():
    print(f'\n----- Меню таблицы "Departments"-----')
    print(f'1. Добавить новый факультет.')
    print(f'2. Найти существующий факультет.')
    print(f'3. Обновить существующий факультет.')
    print(f'4. Удалить существующий факультет.')
    print(f'5. Вывести на экран список всех факультетов.')
    print(f'6. Выйти из программы.')           

def get_menu_dep():
    choice_CRUD_Dep=int(input('Введите ваш вариант: '))
    while choice_CRUD_Dep < MIN_CHOICE or choice_CRUD_Dep > MAX_CHOICE:
        print(f'Допустимые варианты: {MIN_CHOICE} - {MAX_CHOICE}.')
        choice_CRUD_Dep = int(input('Введите ваш вариант: '))
    return choice_CRUD_Dep
    
def new_dep():
    print(f'Добавить новый факультет.')
    name_dep=input('Название факультета: ')
    insert_row_dep(name_dep)
    
def find_dep():
    name_dep=input(f'Введите название искомого факультета: ')
    num_found=display_find_dep(name_dep)
    print(f'{num_found} строк(а) найдено.')
    
def update_dep():
    find_dep()
    selected_id_dep=int(input(f'Выберите ID обновляемой позиции: '))
    name_dep=input(f'Введите новое название факультета: ')
    update_row_dep(name_dep, selected_id_dep)
    
def delete_dep():
    find_dep()
    selected_id_dep=int(input(f'Выберите ID удаляемой позиции: '))
    sure=input('Вы уверены, что хотите удалить данную позицию? (д/н): ')
    if sure.lower()=='д':
        delete_row_dep(selected_id_dep)
        
def show_dep():
    conn=None
    try:
        conn=sqlite3.connect('student_info.db')
        cur=conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''SELECT * FROM Departments''')
        results = cur.fetchall()
        print(f'***********************************')
        for row in results:
            print(f'ID: {row[0]:<2} Факультет: {row[1]:<15}')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn!=None:
            conn.close()
            

def insert_row_dep(name_dep):
    conn=None
    try:
        conn=sqlite3.connect('student_info.db')
        cur=conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''INSERT INTO Departments (Name)
                    VALUES (?)''',
                    (name_dep,))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn!=None:
            conn.close()

def display_find_dep(name_dep):
    conn=None
    results=[]
    try:
        conn=sqlite3.connect('student_info.db')
        cur=conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''SELECT * FROM Departments
                    WHERE Name == ?''',
                    (name_dep, ))
        results=cur.fetchall()
        print(f'****************************************')
        for row in results:
            print(f'ID: {row[0]:<3} Факультет: {row[1]:<15}')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn!=None:
            conn.close()
            return len(results)
            
def update_row_dep(name_dep, selected_id_dep):
    conn=None
    try:
        conn=sqlite3.connect('student_info.db')
        cur=conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''UPDATE Departments
                    SET Name = ?
                    WHERE DepartmentID == ?''',
                    (name_dep, selected_id_dep))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn!=None:
            conn.close()
            
def delete_row_dep(selected_id_dep):
    conn=None
    try:
        conn=sqlite3.connect('student_info.db')
        cur=conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''DELETE FROM Departments
                    WHERE DepartmentID ==?''',
                    (selected_id_dep, ))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn!=None:
            conn.close()
    
make_CRUD_Dep()
