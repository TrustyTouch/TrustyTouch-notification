import psycopg2
from flask import current_app

def get_db_connection():
    return psycopg2.connect(
        dbname=current_app.config['DB_NAME'],
        user=current_app.config['DB_USER'],
        password=current_app.config['DB_PASSWORD'],
        host=current_app.config['DB_HOST']
    )

def send_notification(user_id, message):
    print(f"Sending notification to user {user_id}: {message}")
    return True

def get_unread_notifications(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, message, created_at FROM notifications WHERE user_id = %s AND read_status = FALSE", (user_id,))
        notifications = cur.fetchall()
        if notifications:
            cur.execute("UPDATE notifications SET read_status = TRUE WHERE user_id = %s AND read_status = FALSE", (user_id,))
            conn.commit()
        return [{'id': row[0], 'message': row[1], 'created_at': row[2]} for row in notifications]
    finally:
        cur.close()
        conn.close()