def chat(user_input):
    user_input = user_input.lower()

    if "issue" in user_input:
        return "To issue a book, select option 4 and enter the Book ID and Member ID."

    elif "return" in user_input:
        return "To return a book, select option 5 and enter the Transaction ID."

    elif "add book" in user_input:
        return "Select option 1 and enter the book details."

    elif "member" in user_input:
        return "Select option 3 to add a new member."

    elif "view books" in user_input:
        return "Select option 2 to view all books."

    elif "exit" in user_input:
        return "Select option 8 to exit the program."

    else:
        return "Sorry, I don't understand your question."