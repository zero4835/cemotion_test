import csv
import random
from cemotion import Cemotion

# Initialize the sentiment analyzer
c = Cemotion()

# Generate random userid (1 to 100) and location_id (1 to 10)
def generate_random_data():
    userid = random.randint(1, 100)
    location_id = random.randint(1, 10)
    return userid, location_id
    
# Generate scores (sentiment_score) based on sentiment analysis results
def generate_scores(text):
    sentiment_score = c.predict(text)
    return sentiment_score

# Open the input CSV file and the target output CSV file
input_csv_file = "./comments_100.csv"  # Replace with the path to your CSV file
output_csv_file = "./output.csv"  # Path for the newly generated CSV file

with open(input_csv_file, "r", encoding="utf-8") as input_file, open(
    output_csv_file, "w", encoding="utf-8", newline=""
) as output_file:
    csv_reader = csv.DictReader(input_file)
    fieldnames = ["userid", "location_id", "sentiment_score", "text"]  # Add 'text' column
    csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    # Iterate through each row in the original CSV file
    for row in csv_reader:
        text = row["text"]  # Assuming "text" is the column name in the CSV

        # Generate random userid and location_id
        userid, location_id = generate_random_data()

        # Generate sentiment scores (sentiment_score) based on sentiment analysis
        sentiment_score = generate_scores(text)

        # Write the results to the new CSV file, including the predicted text
        csv_writer.writerow(
            {
                "userid": userid,
                "location_id": location_id,
                "sentiment_score": sentiment_score,
                "text": text,
            }
        )

print("CSV file has been generated:", output_csv_file)
