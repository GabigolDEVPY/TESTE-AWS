from db import get_connection

def return_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")   
    return cursor.fetchall()