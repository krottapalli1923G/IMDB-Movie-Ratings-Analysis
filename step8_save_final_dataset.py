import pandas as pd

# ✅ Step 8.1: Load the Cleaned Dataset
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

# ✅ Step 8.2: Save the Final Processed Dataset
final_dataset_path = "/Users/krishnanjalikrottapalli/Documents/DataAnalystProject/final_movies_dataset.csv"

try:
    # Save the final dataset
    df.to_csv(final_dataset_path, index=False)
    print(f"\n✅ Final processed dataset saved successfully as '{final_dataset_path}'")

except Exception as e:
    print(f"❌ Error saving final dataset: {e}")
    exit()

