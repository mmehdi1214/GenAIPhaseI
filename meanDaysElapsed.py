import pandas as pd
from datetime import datetime

def load_data():
    """Load data from forms1.csv."""
    return pd.read_csv('forms1.csv')

def preprocess_data(df):
    """Convert the 'created' column to datetime and calculate days elapsed."""
    df['Created'] = pd.to_datetime(df['Created'])
    df['days_elapsed'] = (datetime.now() - df['Created']).dt.days
    return df

def mean_days_by_project(df):
    """Compute mean number of days elapsed since forms were opened by project."""
    return df.groupby('Project')['days_elapsed'].mean()

if __name__ == "__main__":
    df = load_data()
    df = preprocess_data(df)
    mean_days = mean_days_by_project(df)
    
    print("Mean number of days elapsed since forms were opened by project:")
    print(mean_days)
