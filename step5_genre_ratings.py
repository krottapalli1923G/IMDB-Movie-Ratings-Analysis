import pandas as pd
import numpy as np
import ast
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Step 5.1: Load the Cleaned Dataset
cleaned_file_path = "/Users/krishnanjalikrottapalli/Documents/DataAnalystProject/cleaned_movies_metadata.csv"

try:
    # Load the cleaned dataset
    df = pd.read_csv(cleaned_file_path)
    print("✅ Cleaned dataset loaded successfully!")

    # Display dataset overview
    print("\n📊 Dataset Overview:")
    print(df.info())

    # Show first few rows
    print("\n📝 First 5 rows of the dataset:")
    print(df.head())

except FileNotFoundError:
    print("❌ File not found! Check the path and try again.")
    exit()
except Exception as e:
    print(f"❌ Error loading file: {e}")
    exit()

# ✅ Step 5.2: Compute Average Rating Per Genre
df["genres"] = df["genres"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

# Create a dictionary to store ratings for each genre
genre_ratings = {}

# Iterate over each row to accumulate ratings for each genre
for _, row in df.iterrows():
    for genre in row["genres"]:
        if genre not in genre_ratings:
            genre_ratings[genre] = []
        genre_ratings[genre].append(row["vote_average"])

# Compute average rating per genre
avg_genre_ratings = {genre: np.mean(ratings) for genre, ratings in genre_ratings.items()}

# Convert to DataFrame for easy analysis
genre_df = pd.DataFrame(avg_genre_ratings.items(), columns=["Genre", "Average Rating"])
genre_df = genre_df.sort_values(by="Average Rating", ascending=False)

# Display genre ratings
print("\n🎭 Average Rating Per Genre:")
print(genre_df)

# ✅ Step 5.3: Save the Results to a CSV File
genre_ratings_file = "/Users/krishnanjalikrottapalli/Documents/DataAnalystProject/average_genre_ratings.csv"

try:
    # Save the average rating per genre to CSV
    genre_df.to_csv(genre_ratings_file, index=False)
    print(f"\n✅ Average genre ratings saved successfully as '{genre_ratings_file}'")

except Exception as e:
    print(f"❌ Error saving genre ratings: {e}")
    exit()

# ✅ Step 5.4: Visualize the Genre Ratings
plt.figure(figsize=(12, 6))
sns.barplot(x="Average Rating", y="Genre", data=genre_df, palette="coolwarm")
plt.title("🎭 Average Rating Per Genre")
plt.xlabel("Average Rating")
plt.ylabel("Genre")
plt.show()

