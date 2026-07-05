import mysql.connector

def show_analytics():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Myproj@123",
        database="library_db"
    )

    cursor = conn.cursor()

    # Total Books
    cursor.execute("SELECT COUNT(*) FROM books")
    total_books = cursor.fetchone()[0]

    # Total Members
    cursor.execute("SELECT COUNT(*) FROM members")
    total_members = cursor.fetchone()[0]

    print("\n========== LIBRARY ANALYTICS ==========")
    print("Total Books   :", total_books)
    print("Total Members :", total_members)

    cursor.close()
    conn.close()