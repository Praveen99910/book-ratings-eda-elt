# 📚 Book Ratings EDA & ELT  

This project applies *Exploratory Data Analysis (EDA)* and *ELT (Extract, Load, Transform)* techniques on datasets containing *books, users, and ratings*. The goal is to clean, transform, and analyze the data to extract meaningful insights about user reading patterns, book popularity, and rating distributions.  

---

## 📂 Dataset  
The project uses three CSV files:  
- books.csv – Contains book details (title, author, year, publisher, etc.)  
- users.csv – Contains user information (user ID, location, age)  
- ratings.csv – Contains user ratings for books (user ID, book ID, rating)  

---

## ⚙ Technologies Used  
- *Python*  
- *Pandas, NumPy* – Data cleaning and transformation  
- *Matplotlib, Seaborn* – Data visualization  
- *Jupyter Notebook* – Interactive analysis  

---

## 🛠 Process  
1. *Extract* – Imported CSV files into Pandas DataFrames.  
2. *Load* – Verified and structured datasets for consistency.  
3. *Transform* –  
   - Handled missing values and duplicates.  
   - Normalized column names.  
   - Merged ratings, users, and books datasets.  
4. *EDA* –  
   - Analyzed rating distributions.  
   - Identified top-rated and most popular books.  
   - Explored user demographics (age, location, preferences).  
   - Visualized key trends with charts.  

---

## 📊 Key Insights  
- Most users gave ratings between *6–8*.  
- Certain books/authors received consistently higher ratings.  
- Younger users tended to give more ratings compared to older age groups.  
- Data preparation can support a *recommendation system*.  

