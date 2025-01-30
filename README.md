# 🎬 IMDb Movie Ratings Analysis  

## 📊 Project Overview  
This project analyzes IMDb movie ratings to uncover insights such as:  
- **Top 10 highest-rated movies**  
- **Average rating per genre**  
- **Movies with extremely high or low ratings**  
- **Distribution of IMDb ratings**  
- **Data visualizations using Matplotlib & Seaborn**  

The dataset is processed to identify trends, and the final results are saved in CSV files with visualizations.

---

## 📂 Project Structure  
MDb-Movie-Ratings-Analysis/ │-- movies_metadata.csv # Original IMDb dataset
│-- cleaned_movies_metadata.csv # Cleaned dataset
│-- top_10_movies.csv # Top 10 highest-rated movies
│-- average_genre_ratings.csv # Average rating per genre
│-- highly_rated_movies.csv # Movies with ratings >= 9.0
│-- lowly_rated_movies.csv # Movies with ratings <= 3.0
│-- ratings_distribution.png # Histogram of rating distribution
│-- step1_setup.py # Install required dependencies
│-- step2_download.py # Download dataset (manual step)
│-- step3_load_clean.py # Load & clean dataset
│-- step4_top_movies.py # Find top 10 highest-rated movies
│-- step5_genre_ratings.py # Compute average ratings per genre
│-- step6_extreme_ratings.py # Identify extreme ratings
│-- step7_ratings_distribution.py # Plot ratings distribution
│-- step8_save_final_dataset.py # Save final dataset


---

## 🚀 How to Run the Project  
### **1️⃣ Install Required Dependencies**
Run this command in **Terminal** to install required libraries:  
```bash
pip install pandas numpy matplotlib seaborn tabulate
2️⃣ Run the Analysis Scripts
To process and analyze the dataset, execute these scripts in order:

python step3_load_clean.py        # Load and clean the dataset
python step4_top_movies.py        # Find the top 10 highest-rated movies
python step5_genre_ratings.py     # Compute average ratings per genre
python step6_extreme_ratings.py   # Identify movies with extreme ratings
python step7_ratings_distribution.py  # Plot IMDb ratings distribution
python step8_save_final_dataset.py    # Save the final processed dataset
3️⃣ View Results
CSV Files: Processed results are saved in .csv format inside the project folder.
Visualization: ratings_distribution.png shows a histogram of IMDb ratings.
📊 Sample Visualizations

📝 Dataset Information
The dataset used in this project is sourced from IMDb and contains information such as:

Movie Titles
IMDb Ratings (vote_average)
Vote Counts (vote_count)
Genres
📜 License
This project is for educational purposes only. IMDb data is publicly available, but please check their terms of service for usage policies.

🤝 Contributing
Contributions are welcome! If you find any issues or have suggestions, feel free to create a Pull Request or open an Issue.

📌 Contact
👤 Krishnanjali. Krottapalli
📧 Email: [kanjali1923@gmail.com]
🔗 GitHub: https://github.com/krottapalli1923G/IMDB-Movie-Ratings-Analysis
