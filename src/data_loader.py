import pandas as pd
import os

DATA_DIR = "data/raw/mind-small/train"

def load_news():
    """Load news metadata."""
    news_path = os.path.join(DATA_DIR, "news.tsv")
    news_df = pd.read_csv(news_path, sep="\t")
    return news_df

def load_behaviors():
    """Load user interactions (train data)."""
    behaviors_path = os.path.join(DATA_DIR, "behaviors.tsv")
    behaviors_df = pd.read_csv(behaviors_path, sep="\t")
    return behaviors_df

news_df = load_news()
behaviors_df = load_behaviors()

print(news_df.head())
print(behaviors_df.head())