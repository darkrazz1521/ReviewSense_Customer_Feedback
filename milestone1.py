import pandas as pd
import re
import string

STOPWORDS={
    "is","are","the","a","an","to","of","in","on","for","with","this","that",
    "it","was","as","at","be","by","from","or","but","and"
}

def clean_text(text):
    text = str(text).lower()
    text= re.sub(r"http\S+","",text)
    text=re.sub(r"\d+","",text)
    text=text.translate(str.maketrans("","",string.punctuation))
    text=re.sub(r"\s+"," ",text).strip()
    words = [W for W in text.split() if W not in STOPWORDS ]
    return " ".join(words)

def main():
    file_path_excel="ReviewSense_Customer_Feedback_5000.xlsx"
    file_path_csv="Milestone1_cleaned_feedback.csv"

    try:
        df =pd.read_excel(file_path_excel)
        print("Reading from Excel file")

    except FileNotFoundError:
        print("Excel file not found. Attempting to read existing CSV.")
        try:
            df=pd.read_csv(file_path_csv)
            if "clean_feedback" in df.columns:
                print("CSV already has cleaned feedback.Skipping cleaning.")
                return
            elif "feedback" in df.columns:
                print("Re-cleaning feedback from CSV.")
            else:
                raise ValueError("'feedback' column not found in csv file")
        except FileNotFoundError:
            raise ValueError("Neither Excel nor CSV file found. Please provide the input file.")
    
    if "feedback" not in df.columns:
        raise ValueError("feedback not found in columns.")
    df["clean_feedback"] = df["feedback"].apply(clean_text)
    df.to_csv(file_path_csv, index=False)

    print("\n===============================")
    print(" Milestone 1 Completed ")
    print(df[["feedback","clean_feedback"]].head())

if __name__ == "__main__":
    main()
