import sqlite3
conn = sqlite3.connect ('Товары.db')
cur = conn.cursor()

#cur.execute("""CREATE TABLE IF NOT EXISTS Товары(
 #   Наименование TEXT,
 #   Цена FLOAT,
 #   Общее количество INT);
#""")
#conn.commit ()

cur.execute ("""CREATE TABLE IF NOT EXISTS Товары (
    Наименование TEXT,
    Цвет TEXT,
    Размер TEXT,
    Количество INT,
    Цена FLOAT);
""")
conn.commit()
print ('база данных создана')
conn . close ()