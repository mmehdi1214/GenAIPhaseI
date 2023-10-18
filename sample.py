# Import necessary libraries
import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [23, 45, 12, 34]

# Create bar chart
plt.bar(categories, values, color=['blue', 'green', 'red', 'yellow'])

# Add title and labels to the axes
plt.title('Sample Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# Display the bar chart
plt.show()
