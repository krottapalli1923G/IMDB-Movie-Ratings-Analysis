import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Step 7.1: Load the Cleaned Dataset
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

# ✅ Step 7.2: Plot the Ratings Distribution
plt.figure(figsize=(10, 5))

# Plot histogram of ratings
sns.histplot(df["vote_average"], bins=20, kde=True, color="skyblue")

# Add titles and labels
plt.title("Distribution of IMDb Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")

# Show the plot
plt.show()

# ✅ Step 7.3: Save the Plot as an Image
plot_file = "/Users/krishnanjalikrottapalli/Documents/DataAnalystProject/ratings_distribution.png"

try:
    plt.figure(figsize=(10, 5))
    sns.histplot(df["vote_average"], bins=20, kde=True, color="skyblue")
    plt.title("Distribution of IMDb Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    plt.savefig(plot_file)

    print(f"\n✅ Ratings distribution plot saved as '{plot_file}'")

except Exception as e:
    print(f"❌ Error saving plot: {e}")
    exit()

