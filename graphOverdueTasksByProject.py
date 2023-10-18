import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    """Load data from CSV files."""
    df_tasks = pd.read_csv('Tasks.csv')
    return df_tasks

def preprocess_data(df_tasks):
    """Preprocess data and handle missing values."""
    df_tasks = df_tasks[df_tasks['OverDue'].notna()]
    df_tasks['OverDue'] = df_tasks['OverDue'].astype(str)
    print(df_tasks);
    return df_tasks

def get_overdue_by_project(df_tasks):
    """Get number of overdue tasks grouped by project."""
    overdue_tasks = df_tasks[df_tasks['OverDue'].str.lower() == "true"]
    return overdue_tasks.groupby('project').size()

def plot_overdue_by_project(overdue_by_project):
    """Plot a bar chart for overdue tasks by project."""
    projects = overdue_by_project.index.astype(str)
    plt.figure(figsize=(10, 6))
    overdue_by_project.plot(kind='bar', color='blue')
    plt.title('Total Number of Overdue Tasks by Project')
    plt.xlabel('Project Name')
    plt.ylabel('Number of Overdue Tasks')
    plt.xticks(range(len(projects)), projects, rotation=45)
    plt.tight_layout()
    plt.show()
    
def compute_overdue_percentage(df_tasks, overdue_by_project):
    """Compute the percentage of overdue tasks by project."""
    total_tasks_by_project = df_tasks.groupby('project').size()
    overdue_percentage = (overdue_by_project / total_tasks_by_project) * 100
    return overdue_percentage

def plot_overdue_percentage(overdue_percentage):
    """Plot a percentage bar chart for overdue tasks by project."""
    projects = overdue_percentage.index.astype(str)
    plt.figure(figsize=(10, 6))
    overdue_percentage.plot(kind='bar', color='green')
    plt.title('Percentage of Overdue Tasks by Project')
    plt.xlabel('Project Name')
    plt.ylabel('Percentage of Overdue Tasks')
    plt.xticks(range(len(projects)), projects, rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df_tasks = load_data()
    df_tasks = preprocess_data(df_tasks)
    overdue_by_project = get_overdue_by_project(df_tasks)
    plot_overdue_by_project(overdue_by_project)
    overdue_percentage = compute_overdue_percentage(df_tasks, overdue_by_project)
    plot_overdue_percentage(overdue_percentage)
