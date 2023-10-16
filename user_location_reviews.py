import os
import csv
import random
from cemotion import Cemotion

#init
c = Cemotion()

# set location_name, id
location_mapping = {}

# It's all file
location_comment_folder = 'location_comment'
files = os.listdir(location_comment_folder)

# predict text sentiment score
def generate_scores(text):
    sentiment_score = c.predict(text)
    return sentiment_score

# create output file to save result
with open('output.csv', 'w', newline='') as csv_file:
    fieldnames = ['UserId', 'locationId', 'locationName', 'sentiment_score', 'text']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # classify locationId
    with open('./location_comment/location.txt', 'r') as location_file:
        locations = location_file.read().splitlines()
        for i, location in enumerate(locations, start=1):
            # print(location)
            location_mapping[location] = i
            # print(location_mapping)

    # Process each file
    for file in files:
        # print(file)
        location_name, _ = os.path.splitext(file)
        location_name1 = location_name.replace("comment", "").strip()
        print(location_name1)
        location_id = location_mapping.get(location_name1, -1)
        # print(location_id)

        if location_id != -1:
            with open(os.path.join(location_comment_folder, file), 'r') as comment_file:
                comments = comment_file.read().splitlines()
                # print(comments)
                for comment in comments:
                    # print(comment)
                    user_id = random.randint(1, 100)  # 随机生成1到100的userId
                    sentiment_score = generate_scores(comment)

                    # write into output file
                    writer.writerow({
                        'UserId': user_id,
                        'locationId': location_id,
                        'locationName': location_name1,
                        'sentiment_score': sentiment_score,
                        'text': comment
                    })
