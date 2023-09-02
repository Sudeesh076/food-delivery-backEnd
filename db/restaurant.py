import uuid
import sqlite3 


def add_restaurant(data):
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()
    restaurant_id = str(uuid.uuid4())

    cursor.execute('''INSERT INTO restaurants (id, name, caption, logoUrl, email, password, city)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (restaurant_id, data['name'], data['caption'], data['logoUrl'], data['email'], data['password'], data['city']))
    db.commit()
    db.close()


def fetch_restaurant_records():
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM restaurants")
    records = cursor.fetchall()

    records_without_credentials = []
    for record in records:
        record_dict = {
            "id": record[0],
            "name": record[1],
            "caption": record[2],
            "logoUrl": record[3],
            "city": record[6]
        }
        records_without_credentials.append(record_dict)

    db.close()
    return records_without_credentials


def fetch_restaurant_by_id(restaurant_id):
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM restaurants WHERE id = ?", (restaurant_id,))
    record = cursor.fetchone()

    if record is None:
        db.close()
        return None

    restaurant_dict = {
        "id": record[0],
        "name": record[1],
        "caption": record[2],
        "logoUrl": record[3],
        "city": record[6]
    }

    db.close()
    return restaurant_dict


def fetch_restaurants_by_city(city_name):
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM restaurants WHERE city = ?", (city_name,))
    records = cursor.fetchall()

    records_without_credentials = []
    for record in records:
        record_dict = {
            "id": record[0],
            "name": record[1],
            "caption": record[2],
            "logoUrl": record[3],
            "city": record[6]
        }
        records_without_credentials.append(record_dict)

    db.close()
    return records_without_credentials





