import sqlite3

def main():

    conn = sqlite3.connect('student_info.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Majors (MajorID INTEGER PRIMARY KEY NOT NULL,
                                                        Name TEXT)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Departments (DeptID INTEGER PRIMARY KEY NOT NULL,
                                                            Name TEXT)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Students (StudentID INTEGER PRIMARY KEY NOT NULL,
                                                        Name TEXT,
                                                        MajorID INTEGER,
                                                        DeptID INTEGER,
                                                        FOREIGN KEY (MajorID) REFERENCES
                                                        Majors (MajorID),
                                                        FOREIGN KEY (DeptID) REFERENCES
                                                        Departments (DeptID))''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
