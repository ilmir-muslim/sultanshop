import sqlite3

def updatedata (data):
    try :
        conn = sqlite3.connect ('Товары.db')        
        cur = conn.cursor()
        print("Подключен к SQLite")
        
        sqlite3_update_data = ("""UPDATE Товары SET Количество = ? WHERE Наименование = ?, Цвет = ?, Размер = ?""")
        # не заботает, нужно выяснить способ выбора строки для обновления с несколькими условиями
        cur.execute(sqlite3_update_data, data)
        conn.commit ()
        print ('запись успешно обновлена')
        cur.close()
    
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if conn:
            conn.close()
            print("Соединение с SQLite закрыто")