import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Myproj@123",
    database="library_db"
)

cursor = conn.cursor()

def show_popular_books():

    query = """
    SELECT
        b.title,
        COUNT(i.book_id) AS total_issues
    FROM books b
    JOIN issued_books i
        ON b.book_id = i.book_id
    GROUP BY b.book_id, b.title
    ORDER BY total_issues DESC;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    print("\n========== MOST ISSUED BOOKS ==========\n")

    for row in rows:
        print(f"{row[0]}  -->  {row[1]} issue(s)")