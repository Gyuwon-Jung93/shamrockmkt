import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()

    with open("database_setup.sql", "r") as sql_file:
        cur.execute(sql_file.read())

    conn.commit()
    print("✅ Database tables created successfully!")

except Exception as e:
    print(f"⚠️ Error occurred while setting up the database: {e}")

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()