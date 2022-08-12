import sqlite3

def main():

    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Entries (EntryID INTEGER PRIMARY KEY NOT NULL,
                                                        Name TEXT,
                                                        PhoneNumber INTEGER)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
