import pandas as pd
import numpy as np
import ast

# ✅ Step 3.1: Load the Dataset
# Define the file path (Update if needed)
file_path = "/Users/krishnanjalikrottapalli/Documents/DataAnalystProject/movies_metadata.csv"

try:
    # Load dataset
    df = pd.read_csv(file_path, low_memory=False)
    print("✅ Dataset loaded successfully!")
    
    # Display basic dataset information
    print("\n📊 Dataset Overview:")
    print(df.info())

    # Show first 5 rows
    print("\n📝 First 5 rows of the dataset:")
    print(df.head())

except FileNotFoundError:
    print("❌ File not found! Check the path and try again.")
    exit()
except Exception as e:
    print(f"❌ Error loading file: {e}")
    exit()

# ✅ Step 3.2: Clean the Dataset

# Convert 'vote_average' to numeric format
df["vote_average"] = pd.to_numeric(df["vote_average"], errors="coerce")

# Function to extract genres
def extract_genres(genre_str):
    try:
        genres = ast.literal_eval(genre_str)  # Convert string to list of dictionaries
        return [genre["name"] for genre in genres]  # Extract genre names
    except:
        return []

# Apply genre extraction function
df["genres"] = df["genres"].apply(extract_genres)

# Drop rows with missing values in important columns
df = df[["title", "vote_average", "vote_count", "genres"]].dropna()

# Remove movies with fewer than 10 votes (to remove noise)
df = df[df["vote_count"] > 10]

# ✅ Step 3.3: Save the Cleaned Dataset
cleaned_file_path = "/Users/krishnanjalikrottapalli/Documents/DataAnalystProject/cleaned_movies_metadata.csv"

df.to_csv(cleaned_file_path, index=False)
print(f"\n✅ Cleaned dataset saved successfully as '{cleaned_file_path}'")

# Display cleaned dataset overview
print("\n📊 Cleaned Dataset Overview:")
print(df.info())

# Show first 5 rows after cleaning
print("\n📝 First 5 rows after cleaning:")
print(df.head())

