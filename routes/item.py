from flask import Blueprint, request, jsonify, app

from db.items import add_item, fetch_items_by_restaurant_id

item_bp = Blueprint('item', __name__)


@item_bp.route('/restaurant/<restaurant_id>/item', methods=['POST'])
def new_item(restaurant_id):
    try:
        data = request.json
        if 'name' in data and 'price' in data and 'type' in data and 'imgUrl' in data and 'nutritionalUrl' in data:
            add_item(data, restaurant_id)
            return jsonify({"message": "Item added successfully"}), 201
        else:
            return jsonify({"error": "Missing data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@item_bp.route('/restaurant/<restaurant_id>/items', methods=['GET'])
def get_items_by_restaurant(restaurant_id):
    try:
        items = fetch_items_by_restaurant_id(restaurant_id)
        return jsonify(items), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
