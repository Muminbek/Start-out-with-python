import sqlite3

conn = sqlite3.connect('employees.db')
cur = conn.cursor()

cur.execute('''INSERT INTO Departments(DepartmentName) 
              VALUES ('Accounting'),
                     ('Manafacturing'),
                     ('Marketing'),
                     ('Research and Development')''')

cur.execute('''INSERT INTO Locations(City)
             VALUES ('Austin'),
                    ('Boston'),
                    ('New York City'),
                    ('San Jose')''')

cur.execute('''INSERT INTO Employees(Name, Position, DepartmentID, LocationID) 
             VALUES ('Arlene Meyers', 'Director', 4, 4),
                    ('Janella Grant', 'Engineer', 2, 1),
                    ('Jack Smith', 'Manager', 3, 3),
                    ('Sonia Alvarado', 'Auditor', 1,2),
                    ('Renee Kincaid', 'Designer', 3,3),
                    ('Curt Green', 'Supervisor', 2, 1)''')

conn.commit()
conn.close()