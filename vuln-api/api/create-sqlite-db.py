import sqlite3

DATABASE = "todos.db"
def create_database(DATABASE):
    # connection = sqlite3.connect(DATABASE)
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    # db = get_db()
    # cursor = db.cursor()
    create_user_table = 'CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL);'

    cursor.execute(create_user_table)

    create_todos_table = 'CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY, user TEXT NOT NULL, todo TEXT NOT NULL, date TIMESTAMP);'

    cursor.execute(create_todos_table)

    cursor.execute('INSERT INTO user VALUES(1, "imran", "imran");')
    cursor.execute('INSERT INTO user VALUES(2, "irfan", "irfan");')
    cursor.execute('INSERT INTO user VALUES(3, "yuga", "yuga");')

    cursor.execute("INSERT INTO todos VALUES(1,'irfan','Buy a Lamp','2019-09-10 00:00:00');")
    cursor.execute("INSERT INTO todos VALUES(2,'imran','Buy groceries','2020-08-06 00:00:00');")
    cursor.execute("INSERT INTO todos VALUES(3,'yuga','Buy Laptop','2020-08-07 00:00:00')")

    connection.commit()
    connection.close()

    print('Database successfully created and populated with data!')


# Create the database using the above function
create_database(DATABASE)
