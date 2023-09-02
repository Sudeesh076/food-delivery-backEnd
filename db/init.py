import sqlite3


def startDb():
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    create_orders_table(cursor)
    create_items_table(cursor)
    create_restaurants_table(cursor)
    create_users_table(cursor)
    db.commit()
    db.close()


def create_restaurants_table(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='restaurants'")
    table_exists = cursor.fetchone()

    if table_exists:
        cursor.execute("DROP TABLE restaurants")

    cursor.execute('''CREATE TABLE restaurants (
        id TEXT PRIMARY KEY,
        name TEXT,
        caption TEXT,
        logoUrl TEXT,
        email TEXT UNIQUE,
        password TEXT,
        city TEXT 
    )''')


def create_items_table(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='items'")
    table_exists = cursor.fetchone()

    if table_exists:
        cursor.execute("DROP TABLE items")

    cursor.execute('''CREATE TABLE items (
        id TEXT PRIMARY KEY,
        name TEXT,
        price REAL,
        type TEXT,
        imgUrl TEXT,
        nutritionalUrl TEXT,
        restaurant_id TEXT,
        FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
            ON DELETE RESTRICT
            ON UPDATE CASCADE
    )''')


def create_users_table(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exists = cursor.fetchone()

    if table_exists:
        cursor.execute("DROP TABLE users")

    cursor.execute('''CREATE TABLE users (
        id TEXT PRIMARY KEY,
        email TEXT UNIQUE,
        password TEXT,
        first_name TEXT,
        last_name TEXT,
        ph_number TEXT,
        address TEXT
    )''')


def create_orders_table(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='orders'")
    table_exists = cursor.fetchone()

    if table_exists:
        cursor.execute("DROP TABLE orders")

    cursor.execute('''CREATE TABLE orders (
        id TEXT PRIMARY KEY,
        group_id TEXT,
        user_id TEXT,
        item_id TEXT,
        restaurant_id TEXT,
        createdDateTime TEXT,
        deliveredDateTime TEXT,
        status TEXT,
        FOREIGN KEY (item_id) REFERENCES items (id)
            ON DELETE RESTRICT
            ON UPDATE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users (id)
            ON DELETE RESTRICT
            ON UPDATE CASCADE,
        FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
            ON DELETE RESTRICT
            ON UPDATE CASCADE
    )''')


class ValueNotFoundError(Exception):
    pass


def check_value_exists(value, field_name, table):
    try:
        db = sqlite3.connect("foodDelivery.db")
        cursor = db.cursor()

        query = f"SELECT COUNT(*) FROM {table} WHERE {field_name} = ?"
        cursor.execute(query, (value,))
        result = cursor.fetchone()[0]

        db.close()

        if result > 0:
            return True
        else:
            raise ValueNotFoundError(
                f"The value '{value}' does not exist in the '{field_name}' field of the '{table}' table.")
    except Exception as e:
        raise e
