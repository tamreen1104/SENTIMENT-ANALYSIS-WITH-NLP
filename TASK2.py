import pandas as pd

# Load the dataset
# Replace 'your_reviews.csv' with your actual file path
# Assume your CSV has at least two columns: 'review_text' and 'sentiment_label'
try:
    df = pd.read_csv('your_reviews.csv')
    print("Dataset loaded successfully!")
    print(df.head())
except FileNotFoundError:
    print("Error: 'your_reviews.csv' not found. Please make sure the file is in the correct directory.")
    # Create a dummy DataFrame for demonstration if file not found
    data = {'review_text': [
        "This product is amazing! I love it.",
        "Terrible experience, very disappointed.",
        "It's okay, nothing special.",
        "Highly recommend, great value for money.",
        "Worst purchase ever, a complete waste."
    ],
            'sentiment_label': ['positive', 'negative', 'neutral', 'positive', 'negative']}
    df = pd.DataFrame(data)
    print("Using a dummy dataset for demonstration.")
    print(df.head())

# Check for essential columns
if 'review_text' not in df.columns or 'sentiment_label' not in df.columns:
    print("Error: Dataset must contain 'review_text' and 'sentiment_label' columns.")
    # Exit or raise an error if critical columns are missing
    exit()

# If your sentiment labels are not already numerical (e.g., 'positive', 'negative'),
# you might need to encode them.
# For simplicity, let's assume 'positive' and 'negative' will be mapped to 1 and 0.
df['sentiment_encoded'] = df['sentiment_label'].map({'positive': 1, 'negative': 0, 'neutral': 0.5}) # Adjust for neutral if needed

# For binary classification (positive/negative), you might filter out neutrals or map them to a specific class.
# Let's assume a binary classification for this example: positive vs. negative.
df = df[df['sentiment_label'].isin(['positive', 'negative'])]
df['sentiment_binary'] = df['sentiment_label'].map({'positive': 1, 'negative': 0})

X = df['review_text']
y = df['sentiment_binary']
