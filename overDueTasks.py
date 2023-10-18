import pandas as pd

# =======================
# LOAD DATA
# =======================

# Load tasks data from 'Tasks.csv'
file_path_tasks = 'Tasks.csv'
df_tasks = pd.read_csv(file_path_tasks)

# Load forms data from 'Forms.csv'
file_path_forms = 'Forms.csv'
df_forms = pd.read_csv(file_path_forms)

# =======================
# DATA CLEANING
# =======================

# Ensure there are no missing values in the 'OverDue' column
df_tasks = df_tasks[df_tasks['OverDue'].notna()]

# Convert 'OverDue' column to string type
df_tasks['OverDue'] = df_tasks['OverDue'].astype(str)

# =======================
# DATA ANALYSIS
# =======================

# Filter tasks that are overdue
overdue_tasks = df_tasks[df_tasks['OverDue'].str.lower() == "true"]

# Print the number of overdue tasks
print(f"Total number of tasks that are overdue: {len(overdue_tasks)}")
