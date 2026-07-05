import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Myproj@123",
    database="library_db"
)

cursor = conn.cursor()

def show_history():

    query = """
    SELECT
        i.issue_id,
        b.title,
        m.name,
        i.issue_date,
        i.return_date
    FROM issued_books i
    JOIN books b
        ON i.book_id = b.book_id
    JOIN members m
        ON i.member_id = m.member_id;
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    print("\n========== ISSUE HISTORY ==========\n")

    for row in rows:
        print("Issue ID    :", row[0])
        print("Book        :", row[1])
        print("Member      :", row[2])
        print("Issue Date  :", row[3])
        print("Return Date :", row[4])
        print("-" * 35)