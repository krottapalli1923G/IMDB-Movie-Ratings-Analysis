import pandas as pd
from tabulate import tabulate

# ✅ Step 4.1: Load the Cleaned Dataset
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

# ✅ Step 4.2: Find the Top 10 Highest-Rated Movies
try:
    # Get the top 10 highest-rated movies
    top_movies = df.sort_values(by="vote_average", ascending=False).head(10)

    # Display results
    print("\n🎬 Top 10 Highest-Rated Movies:")
    print(tabulate(top_movies[["title", "vote_average"]], headers="keys", tablefmt="pretty"))

except Exception as e:
    print(f"❌ Error computing top movies: {e}")
    exit()

# ✅ Step 4.3: Save the Results to a CSV File
top_movies_file = "/Users/krishnanjalikrottapalli/Documents/DataAnalystProject/top_10_movies.csv"

try:
    # Save the top 10 movies to CSV
    top_movies.to_csv(top_movies_file, index=False)
    print(f"\n✅ Top 10 movies saved successfully as '{top_movies_file}'")

except Exception as e:
    print(f"❌ Error saving top movies: {e}")
    exit()

