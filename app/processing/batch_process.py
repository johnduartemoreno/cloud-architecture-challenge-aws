import boto3
import pandas as pd
import random
from uuid import uuid4
from decimal import Decimal

# Load the dataset
file_path = "app/ingestion/data/netflix_titles.csv"
data = pd.read_csv(file_path)

# Filter movies for adults (18+)
adult_movies = data[(data["type"] == "Movie") & (data["rating"].isin(["R", "TV-MA", "NC-17"]))]

print(f"Total adult movies: {adult_movies.shape[0]}")

# Audience simulation by age and gender
groups = ["18-30", "31-40", "41-50", "50+"]
genders = ["Male", "Female"]

audience_simulation = []
for _, row in adult_movies.iterrows():
    genre_list = row["listed_in"].split(", ")
    for genre in genre_list:
        genre = genre.strip()
        for group in groups:
            for gender in genders:
                audience_simulation.append({
                    "title": row["title"],
                    "genre": genre,
                    "age_group": group,
                    "gender": gender,
                    "audience_percentage": Decimal(str(round(random.uniform(5, 30), 2)))  # Convert to Decimal
                })

# Create a DataFrame of the simulated audience
audience_df = pd.DataFrame(audience_simulation)

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
TABLE_NAME = "aws-data-ingestion-processed-data"
table = dynamodb.Table(TABLE_NAME)

# Batch write to DynamoDB
with table.batch_writer() as batch:
    for _, row in audience_df.iterrows():
        try:
            batch.put_item(
                Item={
                    "record_id": str(uuid4()),
                    "title": row["title"],
                    "genre": row["genre"],
                    "age_group": row["age_group"],
                    "gender": row["gender"],
                    "audience_percentage": row["audience_percentage"]  # Already Decimal
                }
            )
        except Exception as e:
            print(f"Error inserting record {row['title']}: {e}")

print(f"Records successfully saved to DynamoDB: {len(audience_df)}")
