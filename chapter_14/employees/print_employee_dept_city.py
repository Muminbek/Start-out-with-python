import sqlite3


def main():

    conn = None

    try:

        # Connect to the database and get a cursor.
        conn = sqlite3.connect('employees.db')
        cur = conn.cursor()

        # Enable foreign key enforcement.
        cur.execute('PRAGMA foreign_keys=ON')

        # Retrieve employee names, departments, and cities.
        cur.execute(
            '''SELECT
            Employees.Name,
            Employees.Position,
            Departments.DepartmentName,
            Locations.City
            FROM
            Employees, Departments, Locations
            WHERE
            Employees.DepartmentID == Departments.DepartmentID AND
            Employees.LocationID == Locations.LocationID''')

        results = cur.fetchall()
        for row in results:
            print(f'{row[0]:15} {row[1]:15} {row[2]:25} {row[3]}')

    except sqlite3.Error as err:
        print(err)

    finally:
    # If the connection is open, then close it.
        if conn != None:
            conn.close()

if __name__ == '__main__':
    main()
