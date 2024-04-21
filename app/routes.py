from flask import Blueprint, request, jsonify
from .services import send_notification

notification_bp = Blueprint('notification_bp', __name__)

@notification_bp.route('/notify', methods=['POST'])
def notify():
    data = request.get_json()
    message = data.get('message', '')
    user_id = data.get('user_id', '')
    
    if send_notification(user_id, message):
        return jsonify({"status": "success", "message": "Notification sent"}), 200
    else:
        return jsonify({"status": "failed", "message": "Notification failed"}), 400