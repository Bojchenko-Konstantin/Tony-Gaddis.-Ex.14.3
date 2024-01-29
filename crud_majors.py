import sqlite3

MIN_CHOICE=1
MAX_CHOICE=6
NEW_MAJOR=1
FIND_MAJOR=2
UPDATE_MAJOR=3
DELETE_MAJOR=4
SHOW_ALL_MAJORS=5
EXIT=6

def make_CRUD_Majors():
    choice_CRUD_Majors=0
    while choice_CRUD_Majors !=EXIT:
        display_menu_majors()  
        choice_CRUD_Majors=get_menu_majors()
        
        if choice_CRUD_Majors == NEW_MAJOR:
            new_major()
        elif choice_CRUD_Majors == FIND_MAJOR:
            find_major()
        elif choice_CRUD_Majors == UPDATE_MAJOR:
            update_major()
        elif choice_CRUD_Majors == DELETE_MAJOR:
            delete_major()
        elif choice_CRUD_Majors == SHOW_ALL_MAJORS:
            show_majors() 

def display_menu_majors():
    print(f'\n----- Меню таблицы "Majors"-----')
    print(f'1. Добавить новую специальность.')
    print(f'2. Найти существующую специальность.')
    print(f'3. Обновить существующую специальность.')
    print(f'4. Удалить существующую специальность.')
    print(f'5. Вывести на экран список всех специальностей.')

def get_menu_majors():
    choice_CRUD_Majors=int(input('Введите ваш вариант: '))
    while choice_CRUD_Majors < MIN_CHOICE or choice_CRUD_Majors > MAX_CHOICE:
        print(f'Допустимые варианты: {MIN_CHOICE} - {MAX_CHOICE}.')
        choice_CRUD_Majors = int(input('Введите ваш вариант: '))
    return choice_CRUD_Majors
    
def new_major():
    print(f'Добавить новую специальность.')
    name_major=input('Название специальности: ')
    insert_row_major(name_major)

def find_major():
    name_major=input(f'Введите название искомой специальности.')
    num_found=display_find_major(name_major)
    print(f'{num_found} строк(а) найдено.')

def update_major():
    find_major()
    selected_id_majors=int(input(f'Выберите ID обновляемой позиции: '))
    name_major=input(f'Введите новое название специальности: ')
    update_row_major(name_major, selected_id_majors)
    

def delete_major():
    find_major()
    selected_id_majors=int(input(f'Выберите ID удаляемой позиции: '))
    sure=input('Вы уверены, что хотите удалить данную позицию? (д/н): ')
    if sure.lower()=='д':
        delete_row_major(selected_id_majors)
        
        
def show_majors():
    conn=None
    try:
        conn=sqlite3.connect('student_info.db')
        cur=conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''SELECT * FROM Majors''')
        results = cur.fetchall()
        for row in results:
            print(f'{row[0]:2} {row[1]:35}')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn!=None:
            conn.close() 

def insert_row_major(name_major):
    conn=None
    try:
        conn=sqlite3.connect('student_info.db')
        cur=conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''INSERT INTO Majors (Name)
                    VALUES (?)''',
                    (name_major,))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn!=None:
            conn.close()
            
def display_find_major(name_major):
    conn=None
    results=[]
    try:
        conn=sqlite3.connect('student_info.db')
        cur=conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''SELECT * FROM Majors
                    WHERE Name == ?''',
                    (name_major, ))
        results=cur.fetchall()
        for row in results:
            print(f'ID: {row[0]} Специальность: {row[1]}')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn!=None:
            conn.close()
            return len(results)

def update_row_major(name_major, selected_id_majors):
    conn=None
    try:
        conn=sqlite3.connect('student_info.db')
        cur=conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''UPDATE Majors
                    SET Name = ?
                    WHERE MajorID == ?''',
                    (name_major, selected_id_majors))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn!=None:
            conn.close()
            

def delete_row_major(selected_id_majors):
    conn=None
    try:
        conn=sqlite3.connect('student_info.db')
        cur=conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''DELETE FROM Majors
                    WHERE MajorID ==?''',
                    (selected_id_majors, ))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn!=None:
            conn.close()
    
make_CRUD_Majors()

                    



        
    
    
    
