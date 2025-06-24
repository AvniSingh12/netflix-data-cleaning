Netflix Data Cleaning Task

Dataset
[Netflix Movies and TV Shows from Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)

Objective
Clean the raw dataset by:
- Removing duplicates
- Handling missing values
- Standardizing text data
- Converting date formats
- Renaming columns
- Fixing data types

Summary of Changes
- Dropped duplicate rows
- Filled missing rating with "Not Rated"
- Filled missing director and cast with "Unknown"
- Dropped rows with missing country, release_year, or date_added
- Converted date_added to datetime
- Cleaned column headers (lowercase, snake_case)
- Saved final output as netflix_cleaned.csv

Files
- netflix_titles.csv: Original dataset
- clean_netflix_data.py: Cleaning script
- netflix_cleaned.csv: Cleaned dataset
