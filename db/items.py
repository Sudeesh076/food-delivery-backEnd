import sqlite3
import uuid

from db.init import check_value_exists


def fetch_items_by_restaurant_id(restaurant_id):
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM items WHERE restaurant_id = ?", (restaurant_id,))
    records = cursor.fetchall()

    if not records:
        db.close()
        return []

    items_list = []
    for record in records:
        item_dict = {
            "id": record[0],
            "name": record[1],
            "price": record[2],
            "type": record[3],
            "imgUrl": record[4],
            "nutritionalUrl": record[5]
        }
        items_list.append(item_dict)

    db.close()
    return items_list


def add_item(data, restaurant_id):
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()
    item_id = str(uuid.uuid4())
    check_value_exists(restaurant_id, "id", "restaurants")

    cursor.execute('''INSERT INTO items (id, name, price, type, imgUrl, nutritionalUrl, restaurant_id)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (item_id, data['name'], data['price'], data['type'], data['imgUrl'], data['nutritionalUrl'], restaurant_id))
    db.commit()
    db.close()
