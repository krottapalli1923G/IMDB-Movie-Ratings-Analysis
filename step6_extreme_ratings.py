import pandas as pd
from tabulate import tabulate

# ✅ Step 6.1: Load the Cleaned Dataset
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

# ✅ Step 6.2: Identify Movies with Very High Ratings (≥ 9.0)
highly_rated_movies = df[df["vote_average"] >= 9.0]

print("\n🌟 Movies with Extremely High Ratings:")
print(tabulate(highly_rated_movies[["title", "vote_average"]], headers="keys", tablefmt="pretty"))

# ✅ Step 6.3: Identify Movies with Very Low Ratings (≤ 3.0)
lowly_rated_movies = df[df["vote_average"] <= 3.0]

print("\n💀 Movies with Extremely Low Ratings:")
print(tabulate(lowly_rated_movies[["title", "vote_average"]], headers="keys", tablefmt="pretty"))

# ✅ Step 6.4: Save the Results to CSV Files
high_rated_file = "/Users/krishnanjalikrottapalli/Documents/DataAnalystProject/highly_rated_movies.csv"
low_rated_file = "/Users/krishnanjalikrottapalli/Documents/DataAnalystProject/lowly_rated_movies.csv"

try:
    # Save to CSV files
    highly_rated_movies.to_csv(high_rated_file, index=False)
    lowly_rated_movies.to_csv(low_rated_file, index=False)

    print(f"\n✅ Highly rated movies saved as '{high_rated_file}'")
    print(f"✅ Lowly rated movies saved as '{low_rated_file}'")

except Exception as e:
    print(f"❌ Error saving files: {e}")
    exit()

