📚 Book Recommendation System (KNN + Collaborative Filtering)

This project is a Book Recommendation System built using Python, Pandas, and Scikit-learn.
It suggests similar books based on user rating patterns using K-Nearest Neighbors (KNN) with cosine similarity.

---

🚀 Features

- 📊 Filters high-quality books (minimum 50 ratings)
- 🔄 Uses collaborative filtering (user-based interactions)
- ⚡ Efficient sparse matrix computation
- 🎯 Recommends similar books instantly

---

🧠 How It Works

1. Load Data
   
   - Reads a dataset containing:
     - "user_id"
     - "book_title"
     - "rating"

2. Data Cleaning
   
   - Removes books with fewer than 50 ratings to improve recommendation quality.

3. Pivot Table Creation
   
   - Converts data into a matrix:
     - Rows → Books
     - Columns → Users
     - Values → Ratings

4. Sparse Matrix Conversion
   
   - Optimizes memory using "csr_matrix".

5. Model Training
   
   - Uses KNN (NearestNeighbors) with cosine similarity to find similar books.

6. Recommendation
   
   - Given a book, returns the top 5 similar books.

---

📂 Project Structure

├── ratings.csv          # Dataset file
├── recommendation.py    # Main script
└── README.md            # Project documentation

---

⚙️ Installation

Install required libraries:

pip install pandas numpy scipy scikit-learn

---

📊 Dataset Format

Your "ratings.csv" should look like:

user_id,book_title,rating
1,Harry Potter,5
2,Harry Potter,4
3,The Hobbit,5
...

---

🧪 Usage

Run the script and call the function:

recommend_book("The Catcher in the Rye")

Example Output:

Suggestions for 'The Catcher in the Rye':
- Book A
- Book B
- Book C
- Book D
- Book E

---

🛠️ Function Explained

"recommend_book(book_name)"

- Finds the selected book in the dataset
- Computes similarity with other books
- Returns top 5 similar recommendations

---

📌 Key Concepts Used

- Collaborative Filtering
- Cosine Similarity
- K-Nearest Neighbors (KNN)
- Sparse Matrix Optimization

---

⚠️ Limitations

- Cold start problem (new books/users)
- Requires sufficient rating data
- Accuracy depends on dataset quality

---

🔮 Future Improvements

- Add content-based filtering (genre, author)
- Build a web interface (Flask / Streamlit)
- Improve ranking with weighted scores
- Add user-based recommendations

---

🤝 Contributing

Feel free to fork this repo, improve it, and submit a pull request!

---

📜 License

This project is open-source and free to use.

---

💡 Author Note

This is a simple yet powerful beginner-friendly recommendation system.
Perfect for learning how real-world platforms suggest content.

---
