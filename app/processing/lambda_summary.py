import boto3
from boto3.dynamodb.conditions import Key
import json
import os

# AWS Configuration
TABLE_NAME = os.environ.get("DYNAMODB_TABLE", "aws-data-ingestion-processed-data")

# Connect to DynamoDB
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        # Get summary of adult movies by genre and age group
        response = table.scan()
        items = response.get("Items", [])

        genre_summary = {}
        age_group_summary = {}

        for item in items:
            genre = item["genre"]
            age_group = item["age_group"]
            audience_percentage = float(item["audience_percentage"])

            # Grouping by genre
            if genre not in genre_summary:
                genre_summary[genre] = 0
            genre_summary[genre] += audience_percentage

            # Grouping by age group
            if age_group not in age_group_summary:
                age_group_summary[age_group] = 0
            age_group_summary[age_group] += audience_percentage

        summary = {
            "total_records": len(items),
            "genre_summary": genre_summary,
            "age_group_summary": age_group_summary
        }

        print("Summary generated successfully:", summary)
        
        return {
            "statusCode": 200,
            "body": json.dumps(summary, indent=4)
        }

    except Exception as e:
        print(f"Error processing summary: {str(e)}")
        print("New deployment")) 
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
