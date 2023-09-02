from flask import Blueprint, request, jsonify

from db.order import add_order, update_order_status, fetch_order

order_bp = Blueprint('order', __name__)


@order_bp.route('/order', methods=['POST'])
def addOrder():
    try:
        data = request.json
        if 'user_id' in data and 'item_id_list' in data and 'restaurant_id' in data:
            add_order(data['user_id'], data['item_id_list'], data['restaurant_id'])
            return jsonify({"message": "Order created successfully"}), 201
        else:
            return jsonify({"error": "Missing data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@order_bp.route('/order/<order_id>', methods=['PUT'])
def updateOrderStatus(order_id):
    try:
        data = request.json
        new_status = data.get('status', '').strip()
        if new_status:
            check_status(new_status, order_id)
            update_order_status(order_id, new_status)
            return jsonify({"message": "Order status updated successfully"}), 200
        else:
            return jsonify({"error": "Missing or empty 'status' field in the request body"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@order_bp.route('/order', methods=['GET'])
def fetchOrders():
    try:
        order_id = request.args.get('order_id')
        user_id = request.args.get('user_id')
        restaurant_id = request.args.get('restaurant_id')

        if order_id:
            orders = fetch_order(order_id=order_id)
        elif user_id:
            orders = fetch_order(user_id=user_id)
        elif restaurant_id:
            orders = fetch_order(restaurant_id=restaurant_id)
        else:
            return jsonify({"message": "No parameters provided"}), 400

        if not orders:
            return jsonify({"message": "No orders found"}), 200

        return jsonify(orders), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


class InvalidStatusTransitionError(Exception):
    pass


def check_status(new_status, order_id):
    allowed_statuses = ["Created", "Accepted", "Cancel", "Preparing", "Picked", "Arrived", "Delivered"]

    if new_status not in allowed_statuses:
        raise InvalidStatusTransitionError(f"The Invalid Status: '{new_status}'")

    previous_status = fetch_order(order_id)[0].get("status")

    if previous_status == "Created":
        if new_status not in ["Accepted", "Cancel"]:
            raise InvalidStatusTransitionError(f"Invalid status transition from '{previous_status}' to '{new_status}'")

    elif previous_status == "Accepted":
        if new_status != "Preparing":
            raise InvalidStatusTransitionError(f"Invalid status transition from '{previous_status}' to '{new_status}'")

    elif previous_status == "Preparing":
        if new_status != "Picked":
            raise InvalidStatusTransitionError(f"Invalid status transition from '{previous_status}' to '{new_status}'")

    elif previous_status == "Picked":
        if new_status != "Arrived":
            raise InvalidStatusTransitionError(f"Invalid status transition from '{previous_status}' to '{new_status}'")

    elif previous_status == "Arrived":
        if new_status != "Delivered":
            raise InvalidStatusTransitionError(f"Invalid status transition from '{previous_status}' to '{new_status}'")

    else:
        raise InvalidStatusTransitionError(f"Invalid status: '{previous_status}'")

    return True
