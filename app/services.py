import psycopg2
from flask import current_app

def get_db_connection():
    return psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='postgres',
        host='host.docker.internal',
        port='5434'
    )

def send_notification(user_id, message):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO notifications (user_id, message, read_status) VALUES (%s, %s, FALSE)", (user_id, message))
        conn.commit() 
        print(f"Sending notification to user {user_id}: {message}")
        return True
    except Exception as e:
        print(f"Failed to send notification: {e}")
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()

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