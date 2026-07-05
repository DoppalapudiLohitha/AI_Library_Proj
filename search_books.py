import pandas as pd

books = pd.read_csv("data/books.csv")

def search_book(keyword):
    keyword = keyword.lower()

    results = books[
        books["Title"].str.lower().str.contains(keyword)
    ]

    if len(results) == 0:
        print("\nNo matching books found.")

    else:
        print("\nMatching Books:\n")

        for i, row in results.iterrows():
            print(row["Title"])