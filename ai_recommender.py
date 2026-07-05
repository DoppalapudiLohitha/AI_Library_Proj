import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
books = pd.read_csv("data/books.csv")

# Create a combined text field
books["content"] = books["Title"] + " " + books["Category"]

# Convert text into vectors
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(books["content"])

# Calculate similarity
similarity = cosine_similarity(matrix)

def recommend(book_name):
    book_name = book_name.lower()

    for i, title in enumerate(books["Title"]):
        if title.lower() == book_name:
            scores = list(enumerate(similarity[i]))
            scores = sorted(scores, key=lambda x: x[1], reverse=True)

            print("\nRecommended Books:\n")

            count = 0
            for index, score in scores[1:]:
                print("-", books.iloc[index]["Title"])
                count += 1
                if count == 3:
                    break
            return

    print("Book not found!")