import pandas as pd

# Load dataset
df = pd.read_csv('netflix_titles.csv')

# Initial shape
print("Initial shape:", df.shape)

# 1. Drop duplicates
df.drop_duplicates(inplace=True)

# 2. Handle missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Fill 'rating' with 'Not Rated'
df['rating'].fillna('Not Rated', inplace=True)

# Fill 'director', 'cast' with 'Unknown'
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)

# Drop rows where 'country' or 'date_added' or 'release_year' is missing
df.dropna(subset=['country', 'date_added', 'release_year'], inplace=True)

# 3. Standardize text data
df['type'] = df['type'].str.strip().str.title()
df['country'] = df['country'].str.strip()
df['rating'] = df['rating'].str.upper()

# 4. Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# 5. Clean column names (lowercase, no spaces)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 6. Data types check
print("\nData Types:")
print(df.dtypes)

# Save cleaned data
df.to_csv('netflix_cleaned.csv', index=False)
print("\nCleaned data saved as 'netflix_cleaned.csv'")
