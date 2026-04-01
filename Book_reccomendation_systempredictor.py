
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# 1. Load Data
# Assuming you have a 'ratings.csv' with columns: [user_id, book_title, rating]
ratings = pd.read_csv('ratings.csv')

# 2. Data Cleaning (Filtering for quality)
# Only keep books with at least 50 ratings to avoid obscure suggestions
book_counts = ratings.groupby('book_title').count()['rating']
famous_books = book_counts[book_counts >= 50].index
final_ratings = ratings[ratings['book_title'].isin(famous_books)]

# 3. Create a Pivot Table (Users as columns, Books as rows)
# This creates a matrix where each cell is a user's rating for a specific book
book_pivot = final_ratings.pivot_table(columns='user_id', index='book_title', values='rating')
book_pivot.fillna(0, inplace=True)

# 4. Convert to Sparse Matrix for performance
book_sparse = csr_matrix(book_pivot)

# 5. Build the Model
# We use Cosine Similarity to find "distances" between books
model = NearestNeighbors(algorithm='brute', metric='cosine')
model.fit(book_sparse)

# 6. Function to get recommendations
def recommend_book(book_name):
    # Find the index of the book in our pivot table
    book_id = np.where(book_pivot.index == book_name)[0][0]
    
    # Find the 6 nearest neighbors (the book itself + 5 others)
    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)
    
    print(f"Suggestions for '{book_name}':")
    for i in range(len(suggestions)):
        # Skip the first one because it's the book itself
        books = book_pivot.index[suggestions[i]]
        for j in books[1:]:
            print(f"- {j}")

# Example Usage:
# recommend_book("The Catcher in the Rye")
