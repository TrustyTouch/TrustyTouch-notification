from flask import Blueprint, request, jsonify
from .services import send_notification, get_unread_notifications
from flask_cors import cross_origin

notification_bp = Blueprint('notification_bp', __name__)

@notification_bp.route('/notify', methods=['POST'])
@cross_origin()
def notify():
    data = request.get_json()
    message = data.get('message', '')
    user_id = data.get('user_id', '')
    
    if send_notification(user_id, message):
        return jsonify({"status": "success", "message": "Notification sent"}), 200
    else:
        return jsonify({"status": "failed", "message": "Notification failed"}), 400
    
@notification_bp.route('/notifications/<int:user_id>', methods=['GET'])
@cross_origin()
def fetch_unread_notifications(user_id):
    notifications = get_unread_notifications(user_id)
    if notifications:
        return jsonify({"status": "success", "notifications": notifications}), 200
    else:
        return jsonify({"status": "failed", "message": "No unread notifications"}), 404