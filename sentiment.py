import csv
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_reviews_from_csv(file_path):
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    # TextBlob and VaderSentiment analyzers
    analyzer = SentimentIntensityAnalyzer()

    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            review = row['review_text']

            # TextBlob analysis
            tb_polarity = TextBlob(review).sentiment.polarity

            # VaderSentiment analysis
            vs_results = analyzer.polarity_scores(review)
            vs_compound = vs_results['compound']

            # Determine sentiment categories
            if tb_polarity > 0 or vs_compound > 0.05:
                positive_count += 1
            elif vs_compound < -0.05:
                negative_count += 1
            else:
                neutral_count += 1

    # Calculate overall rating
    overall_sentiment = ""
    if abs(positive_count - negative_count) < 10:
        overall_sentiment = "Neutral"
    elif positive_count > negative_count:
        overall_sentiment = "Positive"
    else:
        overall_sentiment = "Negative"

    return positive_count, negative_count, neutral_count, overall_sentiment

# Usage with CSV file 'reviews.csv'
csv_file_path = 'reviews.csv'
positive_count, negative_count, neutral_count, overall_sentiment = analyze_reviews_from_csv(csv_file_path)

print(f"Number of Positive Reviews: {positive_count}")
print(f"Number of Negative Reviews: {negative_count}")
print(f"Number of Neutral Reviews: {neutral_count}")
print(f"Overall Sentiment: {overall_sentiment}")
