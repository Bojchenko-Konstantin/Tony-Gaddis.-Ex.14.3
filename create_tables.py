import sqlite3

def main():
    conn=sqlite3.connect('student_info.db')
    cur=conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Majors(MajorID INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Departmets(DepartmentID INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS  Students(StudentID INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT,
                                        MajorID INTEGER
                                        DepartmetID INTEGER,
                                        FOREIGN KEY(MajorID) REFERENCES
                                        Majors(MajorID),
                                        FOREIGN KEY(DepartmentID) REFERENCES
                                        Departments(DepartmentID))''')
    conn.commit()
    conn.close()
    
if __name__=='__main__':
    main()

