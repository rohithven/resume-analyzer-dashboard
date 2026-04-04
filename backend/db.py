import mysql.connector

def get_conn():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",          # change if needed
        password="root",
        database="resume_db"
    )
    return conn