import sqlite3

def create_newtab():
    conn=sqlite3.connect('student_info.db')
    cur=conn.cursor()
    cur.execute('PRAGMA foreign_keys=ON')
    cur.execute('''CREATE TABLE IF NOT EXISTS Majors(MajorID INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Departments(DepartmentID INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Students(StudentID INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT,
                                        MajorID INTEGER,
                                        DepartmentID INTEGER,
                                        FOREIGN KEY(MajorID) REFERENCES
                                        Majors(MajorID),
                                        FOREIGN KEY(DepartmentID) REFERENCES
                                        Departments(DepartmentID))''')
    conn.commit()
    conn.close()
    

create_newtab()

