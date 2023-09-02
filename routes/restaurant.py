from flask import Blueprint, request, jsonify
from db.restaurant import add_restaurant, fetch_restaurant_records, fetch_restaurants_by_city

restaurant_bp = Blueprint('restaurant', __name__)


@restaurant_bp.route('/restaurant', methods=['POST'])
def newRestaurant():
    try:
        data = request.json
        if 'name' in data and 'caption' in data and 'logoUrl' in data and 'email' in data and 'password' in data and 'city' in data:
            add_restaurant(data)
            return jsonify({"message": "Record created successfully"}), 201
        else:
            return jsonify({"error": "Missing data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@restaurant_bp.route('/restaurants', methods=['GET'])
def getRestaurants():
    try:
        hotels = fetch_restaurant_records()
        return jsonify(hotels)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@restaurant_bp.route('/restaurants/<city>', methods=['GET'])
def getRestaurantsByCity(city):
    try:
        restaurants = fetch_restaurants_by_city(city)
        return jsonify(restaurants)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
