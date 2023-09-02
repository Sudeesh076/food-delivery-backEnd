import datetime
import sqlite3
import uuid

from db.init import check_value_exists


def add_order(user_id, item_id_list, restaurant_id):
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()
    group_id = str(uuid.uuid4())
    check_value_exists(restaurant_id, "id", "restaurants")
    check_value_exists(user_id, "id", "users")
    for item in item_id_list:
        order_id = str(uuid.uuid4())
        status = "Created"

        createdDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        deliveredDateTime = "null"
        check_value_exists(item, "id", "items")

        cursor.execute('''INSERT INTO orders (
            id, group_id, user_id, item_id, restaurant_id, createdDateTime, deliveredDateTime, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (order_id, group_id, user_id, item, restaurant_id, createdDateTime, deliveredDateTime, status))

    db.commit()
    db.close()


def update_order_status(order_id, new_status):
    try:
        db = sqlite3.connect("foodDelivery.db")
        cursor = db.cursor()

        if new_status.lower() == "Delivered":
            deliveredDateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute('''UPDATE orders
                              SET status = ?, deliveredDateTime = ?
                              WHERE group_id = ?''', (new_status, deliveredDateTime, order_id))
        else:
            cursor.execute('''UPDATE orders
                              SET status = ?
                              WHERE group_id = ?''', (new_status, order_id))

        db.commit()
    except sqlite3.Error as e:
        print("Error updating order status:", e)
    finally:
        db.close()


def fetch_order(order_id=None, user_id=None, restaurant_id=None):
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()

    records = []
    rows = []

    if order_id:
        cursor.execute("SELECT * FROM orders WHERE  group_id= ?", (order_id,))
        rows = cursor.fetchall()
    if user_id:
        cursor.execute("SELECT * FROM orders WHERE  user_id= ?", (user_id,))
        rows = cursor.fetchall()
    if restaurant_id:
        cursor.execute("SELECT * FROM orders WHERE  restaurant_id= ?", (restaurant_id,))
        rows = cursor.fetchall()

    for row in rows:
        record = {
            "id": row[0],
            "order_id": row[1],
            "user_id": row[2],
            "item_id": row[3],
            "restaurant_id": row[4],
            "createdDateTime": row[5],
            "deliveredDateTime": row[6],
            "status": row[7]
        }
        records.append(record)

    return records




