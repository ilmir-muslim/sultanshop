import sqlite3

def selectdataname (name):                                     
    try:
        conn = sqlite3.connect ('Товары.db')        
        cur = conn.cursor()
        
        sqlite3_select_name = "SELECT * FROM Товары WHERE Наименование = ?"
        cur.execute(sqlite3_select_name, (name,))
        records = cur.fetchall()
        conn.commit ()
         
        for row in records:
            print("Наименование товара ", row[0])
            print("Цвет ", row[1])
            print("Размер ", row[2])
            print("Количество ", row[3])
            print("Цена ", row[4], end="\n\n")
        
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if conn:
            conn.close()
            print("Соединение с SQLite закрыто")

def selectdatasize (size):
    try:
        conn = sqlite3.connect ('Товары.db')
        cur = conn.cursor()
        
        sqlite3_select_size = "SELECT * FROM Товары WHERE Размер = ?"
        cur.execute(sqlite3_select_size, (size,))
        records = cur.fetchall()
        conn.commit ()
         
        for row in records:
            print("Наименование товара ", row[0])
            print("Цвет ", row[1])
            print("Размер ", row[2])
            print("Количество ", row[3])
            print("Цена ", row[4], end="\n\n")
        
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if conn:
            conn.close()
            print("Соединение с SQLite закрыто")

def selectdatacolor (color):
    try:
        conn = sqlite3.connect ('Товары.db')
        cur = conn.cursor()
        
        sqlite3_select_color = "SELECT * FROM Товары WHERE Цвет = ?"
        cur.execute(sqlite3_select_color, (color,))
        records = cur.fetchall()
        conn.commit ()
         
        for row in records:
            print("Наименование товара ", row[0])
            print("Цвет ", row[1])
            print("Размер ", row[2])
            print("Количество ", row[3])
            print("Цена ", row[4], end="\n\n")
        
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if conn:
            conn.close()
            print("Соединение с SQLite закрыто")