import sqlite3

MIN_CHOICE=1
MAX_CHOICE=6
NEW_STUD=1
FIND_STUD=2
UPDATE_STUD=3
DELETE_STUD=4
SHOW_ALL_STUD=5
EXIT=6

def make_CRUD_Stud():
    choice_CRUD_Stud=0
    while choice_CRUD_Stud!=EXIT:
        display_menu_stud()  
        choice_CRUD_Stud=get_menu_stud()
        
        if choice_CRUD_Stud == NEW_STUD:
            new_stud()
        elif choice_CRUD_Stud == FIND_STUD:
            find_stud()
        elif choice_CRUD_Stud == UPDATE_STUD:
            update_stud()
        elif choice_CRUD_Stud == DELETE_STUD:
            delete_stud()
        elif choice_CRUD_Stud == SHOW_ALL_STUD:
            show_stud() 
            
def display_menu_stud():
    print(f'\n----- Меню таблицы "Students"-----')
    print(f'1. Добавить нового студента.')
    print(f'2. Найти существующего студента.')
    print(f'3. Обновить существующего студента.')
    print(f'4. Удалить существующего студента.')
    print(f'5. Вывести на экран список всех студентов.')
    print(f'6. Выйти из программы.')
    
def get_menu_stud():
    choice_CRUD_Stud=int(input('Введите ваш вариант: '))
    while choice_CRUD_Stud < MIN_CHOICE or choice_CRUD_Stud > MAX_CHOICE:
        print(f'Допустимые варианты: {MIN_CHOICE} - {MAX_CHOICE}.')
        choice_CRUD_Stud = int(input('Введите ваш вариант: '))
    return choice_CRUD_Stud
    
def new_stud():
    print(f'Добавить нового студента.')
    name_stud=input('ФИО нового студента: ')
    dep_stud_id=input(f'ID факультета на который поступил(а) {name_stud}: ')
    major_stud_id=input('ID специальности: ')
    insert_row_stud(name_stud, dep_stud_id, major_stud_id)
 
def find_stud():
    name_stud=input(f'Введите ФИО искомого студента: ')
    num_found=display_find_stud(name_stud)
    print(f'{num_found} строк(а) найдено.')
    
def display_find_stud(name_stud):
    conn=None
    results=[]
    try:
        conn=sqlite3.connect('student_info.db')
        cur=conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''SELECT * FROM Students
                    WHERE Name == ?''',
                    (name_stud,))
        results=cur.fetchall()
        print(f'*************************************************************')
        for row in results:
            print(f'ID: {row[0]:<3} ФИО студента: {row[1]:<15} ID факультета: {row[2]:<5} ID специальности: {row[3]}')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn!=None:
            conn.close()
            return len(results)
            
def update_stud():
    find_stud()
    selected_id_stud=int(input(f'Выберите ID студента: '))
    newname_stud=input(f'Новое ФИО студента: ')
    dep_id=input(f'Введите ID нового факультета: ')
    major_id=input(f'Введите ID новой специальности: ')
    update_row_stud(newname_stud, dep_id, selected_id_stud, major_id)
    
    
def delete_stud():
    find_stud()
    selected_id_stud=int(input(f'Выберите ID студента для удаления: '))
    sure=input('Вы уверены, что хотите удалить данного студента? (д/н): ')
    if sure.lower()=='д':
        num_deleted = delete_row_stud(selected_id_stud)
        print(f'{num_deleted} строк(а) удалено.')
        
def show_stud():
    conn=None
    try:
        conn=sqlite3.connect('student_info.db')
        cur=conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''SELECT * FROM Students''')
        results = cur.fetchall()
        print(f'*************************************')
        for row in results:
            print(f'ID: {row[0]:<3} ФИО студента: {row[1]:<15} ID факультета: {row[2]:<5} ID специальности: {row[3]}')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn!=None:
            conn.close()
            
def update_row_stud(newname_stud, dep_id, selected_id_stud, major_id):
    conn=None
    try:
        conn=sqlite3.connect('student_info.db')
        cur=conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''UPDATE Students
                    SET Name = ?,
                        MajorID = ?,
                        DepartmentID = ?
                    WHERE StudentID == ?''',
                    (newname_stud, major_id, dep_id, selected_id_stud,))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn!=None:
            conn.close()
        
    
def insert_row_stud(name_stud, dep_stud_id, major_stud_id):
    conn=None
    try:
        conn=sqlite3.connect('student_info.db')
        cur=conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''INSERT INTO Students (Name, DepartmentID, MajorID)
                    VALUES (?, ?, ?)''',
                    (name_stud, dep_stud_id, major_stud_id))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn!=None:
            conn.close()
            
def delete_row_stud(selected_id_stud):
    conn=None
    try:
        conn=sqlite3.connect('student_info.db')
        cur=conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''DELETE FROM Students
                    WHERE StudentID ==?''',
                    (selected_id_stud, ))
        conn.commit()
        num_deleted=cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn!=None:
            conn.close()
        return num_deleted

make_CRUD_Stud()