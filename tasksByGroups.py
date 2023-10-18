import pandas as pd
import matplotlib.pyplot as plt

# =======================
# LOAD DATA
# =======================

# Load tasks data from 'Tasks.csv'
file_path_tasks = 'Tasks1.csv'
df_tasks = pd.read_csv(file_path_tasks)

# =======================
# DATA CLEANING
# =======================

# Ensure there are no missing values in the 'OverDue' column
df_tasks = df_tasks[df_tasks['OverDue'].notna()]

# Convert 'OverDue' column to string type
df_tasks['OverDue'] = df_tasks['OverDue'].astype(str)

# Filter tasks that are overdue
overdue_tasks = df_tasks[df_tasks['OverDue'].str.lower() == "true"]

# Print the number of overdue tasks
print(f"Total number of tasks that are overdue: {len(overdue_tasks)}\n")

# =======================
# DATA ANALYSIS
# =======================

# Group by 'Task Group' and 'Status', then count the number of tasks for each combination
task_group_counts = df_tasks.groupby(['Task Group', 'Status']).size().unstack().fillna(0)

# Combine columns that contain the word 'Open' or 'Closed'
task_group_counts['Open'] = task_group_counts[[col for col in task_group_counts.columns if 'Open' in col]].sum(axis=1)
task_group_counts['Closed'] = task_group_counts[[col for col in task_group_counts.columns if 'Closed' in col]].sum(axis=1)

# Keep only the combined 'Open' and 'Closed' columns for the output
task_group_counts = task_group_counts[['Open', 'Closed']]

print("Total Number of Open and Closed Tasks by Each Task Group:")
print(task_group_counts)

# Print unique values in the 'OverDue' column to understand the data better
unique_overdue_values = df_tasks['OverDue'].unique()
print(f"\nUnique values in the 'OverDue' column: {unique_overdue_values}\n")

task_group_counts.plot(kind='bar', figsize=(10,6))

plt.title('Total Number of Open and Closed Tasks by Each Task Group')
plt.ylabel('Number of Tasks')
plt.xlabel('Task Group')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()