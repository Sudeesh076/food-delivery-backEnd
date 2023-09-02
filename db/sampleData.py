import sqlite3
import uuid
import json


def add_sample_data():
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()

    restaurants_data = [
        (str(uuid.uuid4()), "kfc", "Finger Lickin' Good", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/image1.png", "kfc1@example.com", "kfc_password", "Vadodara"),
        (str(uuid.uuid4()), "pizzahut", "Gather 'Round the Good Stuff", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/image2.png", "ph@example.com", "ph_password", "Vadodara"),
        (str(uuid.uuid4()), "McDonalds", "American - Burgers - Fast Food", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/image3.png", "mc@example.com", "mc_password", "Vadodara"),
        (str(uuid.uuid4()), "UnclePizza", "True Mexican", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/image3.png", "uc@example.com", "uc_password", "Vadodara")
    ]

    items_data = [
        (str(uuid.uuid4()), "Margherita Pizza", 12.99, "veg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/food%2Fpizzabg.png?alt=media","https://example.com/margherita_img.png", restaurants_data[0][0]),
        (str(uuid.uuid4()), "Spicy Chicken Wings", 9.99, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/food%2Ffood2.jpg?alt=media","https://example.com/margherita_img.png", restaurants_data[0][0]),

        (str(uuid.uuid4()), "Classic Pepperoni Pizza", 14.99, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/food%2Ffood3.jpg?alt=media","https://example.com/margherita_img.png", restaurants_data[1][0]),
        (str(uuid.uuid4()), "Veggie Supreme Pizza", 11.99, "veg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/food%2Ffood2.jpg?alt=media","https://example.com/margherita_img.png", restaurants_data[1][0]),

        (str(uuid.uuid4()), "cold coffe", 14.99, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/food%2Ffood3.jpg?alt=media","https://example.com/margherita_img.png", restaurants_data[2][0]),
        (str(uuid.uuid4()), "gold corn pizza", 11.99, "veg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/food%2Ffood3.jpg?alt=media","https://example.com/margherita_img.png", restaurants_data[2][0]),

        (str(uuid.uuid4()), "fried wings", 14.99, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/food%2Ffood3.jpg?alt=media","https://example.com/margherita_img.png", restaurants_data[3][0]),
        (str(uuid.uuid4()), "bbq wing", 11.99, "veg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/food%2Ffood3.jpg?alt=media", "https://example.com/margherita_img.png", restaurants_data[3][0]),
    ]

    for record in restaurants_data:
        cursor.execute("INSERT INTO restaurants (id, name, caption, logoUrl, email, password, city) VALUES (?, ?, ?, ?, ?, ?, ?)", record)

    for record in items_data:
        cursor.execute("INSERT INTO items (id, name, price, type, imgUrl, nutritionalUrl, restaurant_id) VALUES (?, ?, ?, ?, ?, ?, ?)", record)

    users_data = [
        (str(uuid.uuid4()), "user1@example.com", "user1_password", "John", "Doe", "1234567890", "123 Main St"),
        (str(uuid.uuid4()), "user2@example.com", "user2_password", "Jane", "Smith", "9876543210", "456 Elm St")
    ]

    for record in users_data:
        cursor.execute("INSERT INTO users (id, email, password, first_name, last_name, ph_number, address) VALUES (?, ?, ?, ?, ?, ?, ?)", record)

    db.commit()
    db.close()


