import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt


def extract_keywords(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    return words


# --- Main execution ---
if __name__ == "__main__":

    # input from Milestone 2
    df = pd.read_csv("Milestone2_Sentiment_Results_new.csv")

    # --- extract keywords from clean feedback
    all_words = []
    df["clean_feedback"].apply(lambda x: all_words.extend(extract_keywords(x)))

    # --- count keyword frequency
    keyword_freq = Counter(all_words)

    # --- convert to DataFrame
    keywords_df = pd.DataFrame(
        keyword_freq.items(),
        columns=["keyword", "frequency"]
    ).sort_values(by="frequency", ascending=False)

    # save results
    keywords_df.to_csv("Milestone3_Keyword_Insights.csv", index=False)

    print("Milestone 3 completed successfully!")
    print(keywords_df.head(10))

    
     # -------- Visualization using Matplotlib --------
    top_keywords = keywords_df.head(10)

    plt.figure(figsize=(10, 6))
    bars = plt.bar(top_keywords["keyword"], top_keywords["frequency"])

    plt.title("Top 10 Keywords from Customer Feedback")
    plt.xlabel("Keywords")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)

# Add frequency labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,   # center of bar
            height,                              # top of bar
            str(int(height)),                    # frequency value
            ha='center',                         # horizontal align
            va='bottom'                          # vertical align
        )

    plt.tight_layout()
    plt.show()