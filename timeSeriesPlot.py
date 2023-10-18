import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    """Load data from CSV files."""
    df_forms = pd.read_csv('Forms1.csv')
    return df_forms

def preprocess_data(df_forms):
    """Preprocess data and convert 'Created' column to datetime format."""
    df_forms['Created'] = pd.to_datetime(df_forms['Created'])
    return df_forms

def get_report_forms_status_by_group(df_forms):
    """Group data by 'Report Forms Group' and 'Created' date."""
    return df_forms.groupby(['Report Forms Group', 'Created']).size().unstack('Report Forms Group').fillna(0)

def plot_time_series(report_forms_status_by_group):
    """Plot a time series graph for 'Report Forms Status' by 'Report Forms Group'."""
    report_forms_status_by_group.plot(figsize=(10, 6))
    plt.title('Time Series of Report Forms Status by Report Forms Group')
    plt.xlabel('Date Created')
    plt.ylabel('Number of Forms')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df_forms = load_data()
    df_forms = preprocess_data(df_forms)
    report_forms_status_by_group = get_report_forms_status_by_group(df_forms)
    plot_time_series(report_forms_status_by_group)
