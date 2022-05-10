import sqlite3

def inputdata (data):
    try:
        conn = sqlite3.connect ('Товары.db')
        cur = conn.cursor()
        
        cur.execute ("INSERT INTO Товары VALUES(?,?,?,?,?);", (data))
        conn.commit ()
    
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if conn:
            conn.close()
            print("Соединение с SQLite закрыто")