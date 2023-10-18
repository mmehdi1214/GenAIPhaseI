import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    """Load data from Forms1.csv."""
    return pd.read_csv('Forms1.csv')

def filter_open_forms(df):
    """Filter rows where the 'Status' column contains the word 'open'."""
    return df[df['Status'].str.contains('open', case=False, na=False)]

def count_by_type(df):
    """Count the number of open forms by type."""
    return df.groupby('Type').size()

def plot_open_forms_by_type(counts):
    """Plot a bar chart of the number of open forms by type."""
    plt.figure(figsize=(10, 6))
    counts.plot(kind='bar', color='blue')
    plt.title('Number of Open Forms by Type')
    plt.xlabel('Type of Form')
    plt.ylabel('Number of Open Forms')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_data()
    open_forms = filter_open_forms(df)
    counts = count_by_type(open_forms)
    plot_open_forms_by_type(counts)
