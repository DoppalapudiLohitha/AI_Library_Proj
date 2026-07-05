'''
import mysql.connector
from ai_recommender import recommend
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Myproj@123",
        database="library_db")
    if conn.is_connected():
        print("Connected to MySql successfully!")
except mysql.connector.Error as e:
    print("Error:",e)
'''
import mysql.connector
from datetime import datetime
from ai_recommender import recommend
from chatbot import chat
from search_books import search_book
from analytics import show_analytics
from issue_history import show_history
from popular_books import show_popular_books
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Myproj@123",
    database="library_db"
)

cursor = conn.cursor()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Add Member")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. AI Book Recommendation")
    print("7. AI Chatbot")
    print("8. Smart Book Search")
    print("9. Library Analytics")
    print("10. View Issue History")
    print("11. Most Issued Books")
    print("12. Exit")

    choice = input("Enter your choice: ")
    print(choice)

    if choice == "1":
        title=input("Enter Book Title: ")
        author=input("Enter Author: ")
        genre=input("Enter Genre: ")
        total=int(input("Enter Total Copies: "))

        sql="""INSERT INTO Books
            (title,author,genre,total_copies,
            available_copies)
            VALUES(%s,%s,%s,%s,%s)"""
        values=(title,author,genre,total,total)
        cursor.execute(sql,values)
        conn.commit()
        print("Book added successfully!")
               
    elif choice == "2":
        cursor.execute("SELECT * FROM Books")
        books = cursor.fetchall()
        print("\n----- BOOK LIST -----")
        if len(books) == 0:
           print("No books found.")
        else:
          for book in books:
            print(book)

    elif choice == "3":
        name = input("Enter Member Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        join_date = input("Enter Join Date (YYYY-MM-DD): ")
        sql = """INSERT INTO Members
             (name, email, phone, join_date)
             VALUES (%s, %s, %s, %s)"""
        values = (name, email, phone, join_date)
        cursor.execute(sql, values)
        conn.commit()
        print("Member added successfully!")

    elif choice == "4":
         book_id = int(input("Enter Book ID: "))
         member_id = int(input("Enter Member ID: "))
         issue_date = input("Issue Date (YYYY-MM-DD): ")
         due_date = input("Due Date (YYYY-MM-DD): ")
         cursor.execute(
             "SELECT available_copies FROM books WHERE book_id=%s",
             (book_id,)
         )
         result = cursor.fetchone()
         if result is None:
             print("Invalid Book ID!")
             continue
         if result[0] <= 0:
           print("Book is not available!")
           continue
         sql = """INSERT INTO Transactions
         (book_id, member_id, issue_date, due_date)
         VALUES (%s, %s, %s, %s)"""
         values = (book_id, member_id, issue_date, due_date)
         cursor.execute(sql, values)
         cursor.execute("UPDATE Books SET available_copies = available_copies - 1 WHERE book_id=%s",
         (book_id,)
         )
         conn.commit()
         print("Book issued successfully!")

    elif choice == "5":
        txn_id = int(input("Enter Transaction ID: "))
        return_date = input("Return Date (YYYY-MM-DD): ")
        cursor.execute(
            "SELECT due_date FROM Transactions WHERE txn_id=%s",
            (txn_id,)
        )
        due = cursor.fetchone()
        due_date = due[0]
        return_dt = datetime.strptime(return_date, "%Y-%m-%d").date()
        late_days = (return_dt - due_date).days
        if late_days > 0:
            fine = late_days * 10
        else:
            fine = 0
        cursor.execute(
            "UPDATE Transactions SET return_date=%s, fine=%s WHERE txn_id=%s",
            (return_date, fine, txn_id)
        )
        cursor.execute(
             "SELECT book_id FROM Transactions WHERE txn_id=%s",
             (txn_id,)
        )
        book = cursor.fetchone()
        cursor.execute(
            "UPDATE Books SET available_copies = available_copies + 1 WHERE book_id=%s",
            (book[0],)
        )
        conn.commit()
        print("Book returned successfully!")
        print(f"Fine: ₹{fine}")

    elif choice == "6":
          book = input("Enter Book Name: ")
          recommend(book)

    elif choice == "7":
        while True:
            question = input("\nYou: ")

            if question.lower() == "quit":
                print("Bot: Goodbye!")
                break
            response = chat(question)
            print("Bot:", response)
    
    elif choice == "8":
        keyword = input("Enter Keyword: ")
        search_book(keyword)
    
    elif choice == "9":
        show_analytics()
    
    elif choice == "10":
        show_history()
    
    elif choice == "11":
        show_popular_books()
    
    elif choice == "12":
        print("Thank you!")
        break
    else:
        print("Invalid Choice")
cursor.close()
conn.close()
