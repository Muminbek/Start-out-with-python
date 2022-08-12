import sqlite3

conn = sqlite3.connect('employees.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Departments (DepartmentID INTEGER PRIMARY KEY NOT NULL,
                                                    DepartmentName TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Locations (LocationID INTEGER PRIMARY KEY NOT NULL,
                                                    City TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Employees (EmployeeID INTEGER PRIMARY KEY NOT NULL,
                                                    Name TEXT,
                                                    Position TEXT,
                                                    DepartmentID INTEGER,
                                                    LocationID INTEGER,
                                                    FOREIGN KEY(DepartmentID) REFERENCES
                                                                Departments(DepartmentID),
                                                    FOREIGN KEY(LocationID) REFERENCES
                                                                Locations(LocationID))''')
conn.commit()
conn.close()
