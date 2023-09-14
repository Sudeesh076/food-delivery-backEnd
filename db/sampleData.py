import sqlite3
import uuid
import json

from db.order import add_order


def add_sample_data():
    db = sqlite3.connect("foodDelivery.db")
    cursor = db.cursor()

    nu = "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fnutrition.jpg?alt=media"
    d1 = "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fd1.png?alt=media"
    d2 = "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fd2.png?alt=media"
    d3 = "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fd3.png?alt=media"
    d4 = "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fd4.png?alt=media"

    m1 = "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fm1.png?alt=media"
    m2 = "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fm2.png?alt=media"
    m3 = "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fm3.png?alt=media"
    m4 = "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fm4.png?alt=media"


    restaurants_data = [
        (str(uuid.uuid4()), "KFC", "Finger Lickin' Good", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fkfc_log.png?alt=media", "kfcVadodara@gmail.com", "kfcVadodara", "Vadodara"),
        (str(uuid.uuid4()), "Dominos", "Gather 'Round the Good Stuff", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2FDominos_logo.png?alt=media", "dominosVadodara@example.com", "dominosVadodara", "Vadodara"),
        (str(uuid.uuid4()), "McDonalds", "American - Burgers - Fast Food", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2FMcDonald_logo.png?alt=media", "mcdonaldsVadodara@example.com", "mcdonaldsVadodara", "Vadodara"),

        (str(uuid.uuid4()), "KFC", "Finger Lickin' Good", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fkfc_log.png?alt=media", "kfcSurat@example.com", "kfcSurat", "Surat"),
        (str(uuid.uuid4()), "Dominos", "Gather 'Round the Good Stuff", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2FDominos_logo.png?alt=media", "dominosSurat@example.com", "dominosSurat", "Surat"),
        (str(uuid.uuid4()), "McDonalds", "American - Burgers - Fast Food", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2FMcDonald_logo.png?alt=media", "mcdonaldsSurat@example.com", "mcdonaldsSurat", "Surat"),

        (str(uuid.uuid4()), "KFC", "Finger Lickin' Good", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fkfc_log.png?alt=media", "kfcAhmedabad@example.com", "kfcAhmedabad", "Ahmedabad"),
        (str(uuid.uuid4()), "Dominos", "Gather 'Round the Good Stuff", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2FDominos_logo.png?alt=media", "dominosAhmedabad@example.com", "dominosAhmedabad", "Ahmedabad"),
        (str(uuid.uuid4()), "McDonalds", "American - Burgers - Fast Food", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2FMcDonald_logo.png?alt=media", "mcdonaldsAhmedabad@example.com", "mcdonaldsAhmedabad", "Ahmedabad")
    ]

    items_data = [
        (str(uuid.uuid4()), "Peri Peri 10 Leg Pc & 4 Dips", 948.57, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fkfc1.png?alt=media","https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fnutrition.jpg?alt=media", restaurants_data[0][0]),
        (str(uuid.uuid4()), "Chicken Longer Burger & 2 Strips Combo", 219.05, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fkfc2.png?alt=media","https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fnutrition.jpg?alt=media", restaurants_data[0][0]),
        (str(uuid.uuid4()), "Double Chicken Roll & Pepsi Combo", 225.71, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fkfc3.png?alt=media","https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fnutrition.jpg?alt=media", restaurants_data[0][0]),
        (str(uuid.uuid4()), "The Allu Arjun Combo", 448.57, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fkfc4.png?alt=media","https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fnutrition.jpg?alt=media", restaurants_data[0][0]),

        (str(uuid.uuid4()), "Peri Peri 10 Leg Pc & 4 Dips", 948.57, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fkfc1.png?alt=media","https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fnutrition.jpg?alt=media", restaurants_data[3][0]),
        (str(uuid.uuid4()), "Chicken Longer Burger & 2 Strips Combo", 219.05, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fkfc2.png?alt=media","https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fnutrition.jpg?alt=media", restaurants_data[3][0]),
        (str(uuid.uuid4()), "Double Chicken Roll & Pepsi Combo", 225.71, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fkfc3.png?alt=media","https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fnutrition.jpg?alt=media", restaurants_data[3][0]),
        (str(uuid.uuid4()), "The Allu Arjun Combo", 448.57, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fkfc4.png?alt=media","https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fnutrition.jpg?alt=media", restaurants_data[3][0]),

        (str(uuid.uuid4()), "Peri Peri 10 Leg Pc & 4 Dips", 948.57, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fkfc1.png?alt=media","https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fnutrition.jpg?alt=media", restaurants_data[6][0]),
        (str(uuid.uuid4()), "Chicken Longer Burger & 2 Strips Combo", 219.05, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fkfc2.png?alt=media","https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fnutrition.jpg?alt=media", restaurants_data[6][0]),
        (str(uuid.uuid4()), "Double Chicken Roll & Pepsi Combo", 225.71, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fkfc3.png?alt=media","https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fnutrition.jpg?alt=media", restaurants_data[6][0]),
        (str(uuid.uuid4()), "The Allu Arjun Combo", 448.57, "nonVeg", "https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fkfc4.png?alt=media","https://firebasestorage.googleapis.com/v0/b/foodys-34dd3.appspot.com/o/restaurant%2Fnutrition.jpg?alt=media", restaurants_data[6][0]),

        (str(uuid.uuid4()), "FARM HOUSE", 300.00, "Veg", d1, nu, restaurants_data[1][0]),
        (str(uuid.uuid4()), "PEPPY PANEER", 350.00, "Veg", d2, nu, restaurants_data[1][0]),
        (str(uuid.uuid4()), "MEXICAN GREEN WAVE", 500.00, "Veg", d3, nu, restaurants_data[1][0]),
        (str(uuid.uuid4()), "DELUXE VEGGIE", 250.00, "Veg", d4, nu, restaurants_data[1][0]),

        (str(uuid.uuid4()), "FARM HOUSE", 300.00, "Veg", d1, nu, restaurants_data[4][0]),
        (str(uuid.uuid4()), "PEPPY PANEER", 350.00, "Veg", d2, nu, restaurants_data[4][0]),
        (str(uuid.uuid4()), "MEXICAN GREEN WAVE", 500.00, "Veg", d3, nu, restaurants_data[4][0]),
        (str(uuid.uuid4()), "DELUXE VEGGIE", 250.00, "Veg", d4, nu, restaurants_data[4][0]),

        (str(uuid.uuid4()), "FARM HOUSE", 300.00, "Veg", d1, nu, restaurants_data[7][0]),
        (str(uuid.uuid4()), "PEPPY PANEER", 350.00, "Veg", d2, nu, restaurants_data[7][0]),
        (str(uuid.uuid4()), "MEXICAN GREEN WAVE", 500.00, "Veg", d3, nu, restaurants_data[7][0]),
        (str(uuid.uuid4()), "DELUXE VEGGIE", 250.00, "Veg", d4, nu, restaurants_data[7][0]),

        (str(uuid.uuid4()), "Big Mac", 350.00, "nonVeg", m1, nu, restaurants_data[2][0]),
        (str(uuid.uuid4()), "Egg McMuffin", 80.00, "nonVeg", m2, nu, restaurants_data[2][0]),
        (str(uuid.uuid4()), "Sausage Burrito", 230.00, "nonVeg", m3, nu, restaurants_data[2][0]),
        (str(uuid.uuid4()), "Chicken McNuggets", 180.00, "nonVeg", m4, nu, restaurants_data[2][0]),

        (str(uuid.uuid4()), "Big Mac", 350.00, "nonVeg", m1, nu, restaurants_data[5][0]),
        (str(uuid.uuid4()), "Egg McMuffin", 80.00, "nonVeg", m2, nu, restaurants_data[5][0]),
        (str(uuid.uuid4()), "Sausage Burrito", 230.00, "nonVeg", m3, nu, restaurants_data[5][0]),
        (str(uuid.uuid4()), "Chicken McNuggets", 180.00, "nonVeg", m4, nu, restaurants_data[5][0]),

        (str(uuid.uuid4()), "Big Mac", 350.00, "nonVeg", m1, nu, restaurants_data[8][0]),
        (str(uuid.uuid4()), "Egg McMuffin", 80.00, "nonVeg", m2, nu, restaurants_data[8][0]),
        (str(uuid.uuid4()), "Sausage Burrito", 230.00, "nonVeg", m3, nu, restaurants_data[8][0]),
        (str(uuid.uuid4()), "Chicken McNuggets", 180.00, "nonVeg", m4, nu, restaurants_data[8][0]),
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

    add_order(users_data[0][0],
              [items_data[0][0], items_data[1][0], items_data[0][0], items_data[0][0]],
              restaurants_data[0][0])

    add_order(users_data[0][0],
              [items_data[0][0]],
              restaurants_data[0][0])

    add_order(users_data[0][0],
              [items_data[12][0], items_data[13][0], items_data[13][0],items_data[14][0],items_data[14][0]],
              restaurants_data[1][0])

