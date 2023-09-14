import datetime
import sqlite3
import uuid

from db.init import check_value_exists
from db.items import fetch_item_by_id
from db.restaurant import fetch_restaurant_by_id
from db.user import fetch_user_by_id


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
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (order_id, group_id, user_id, item, restaurant_id, createdDateTime, deliveredDateTime, status))

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
            "user_record": fetch_user_by_id(row[2]),
            "item_record": fetch_item_by_id(row[3]),
            "restaurant_record": fetch_restaurant_by_id(row[4]),
            "createdDateTime": row[5],
            "deliveredDateTime": row[6],
            "status": row[7]
        }
        records.append(record)

    return records


def fetch_orders(order_id=None, user_id=None, restaurant_id=None):
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()

    records = []
    rows = []

    if order_id:
        cursor.execute("""select group_id as order_id,B.name as Item,A.restaurant_id,
                        status,createdDateTime,deliveredDateTime,
                        count(item_id) as quantity ,sum(price) as total ,user_id
                        from orders A 
                        LEFT JOIN items B on A.item_id = B.id
                        WHERE  group_id = ?
                        group by group_id , item_id ,B.name , A.restaurant_id , status,createdDateTime,deliveredDateTime,user_id
                        ORDER by createdDateTime DESC""", (order_id,))
        rows = cursor.fetchall()
    if user_id:
        cursor.execute("""select group_id as order_id,B.name as Item,A.restaurant_id,
                        status,createdDateTime,deliveredDateTime,
                        count(item_id) as quantity ,sum(price) as total ,user_id
                        from orders A 
                        LEFT JOIN items B on A.item_id = B.id
                        WHERE  user_id = ?
                        group by group_id , item_id ,B.name ,A.restaurant_id, status,createdDateTime,deliveredDateTime,user_id
                        ORDER by createdDateTime DESC""", (user_id,))
        rows = cursor.fetchall()
    if restaurant_id:
        cursor.execute("""select group_id as order_id,B.name as Item,A.restaurant_id,
                        status,createdDateTime,deliveredDateTime,
                        count(item_id) as quantity ,sum(price) as total ,user_id
                        from orders A 
                        LEFT JOIN items B on A.item_id = B.id
                        WHERE A.restaurant_id = ?
                        group by group_id , item_id ,B.name, A.restaurant_id, status,createdDateTime,deliveredDateTime,user_id
                        ORDER by createdDateTime DESC""", (restaurant_id,))
        rows = cursor.fetchall()

    for row in rows:
        record = {
            "order_id": row[0],
            "status": row[3],
            "createdDateTime": row[4],
            "deliveredDateTime": row[5],
            "itemNames": row[1],
            "quantity": row[6],
            "totalPrice": row[7],
            "restaurant": fetch_restaurant_by_id(row[2]),
            "user": fetch_user_by_id(row[8])
        }
        records.append(record)

    return process_records(records)


def process_records(records):
    grouped_records = {}

    for record in records:
        order_id = record["order_id"]
        if order_id not in grouped_records:
            grouped_records[order_id] = {
                "order_id": order_id,
                "status": record["status"],
                "createdDateTime": record["createdDateTime"],
                "deliveredDateTime": record["deliveredDateTime"],
                "restaurant": record["restaurant"],
                "user": record["user"],
                "itemNames": [],
                "quantity": [],
                "totalPrice": 0
            }
        grouped_records[order_id]["itemNames"].append(record["itemNames"])
        grouped_records[order_id]["quantity"].append(record["quantity"])
        grouped_records[order_id]["totalPrice"] += record["totalPrice"]

    return list(grouped_records.values())
