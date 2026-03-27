import psycopg2

conn = psycopg2.connect(
    host="db",          # 🔥 핵심
    database="mydb",
    user="user",
    password="password",
    port=5432
)

print("DB 연결 성공")
