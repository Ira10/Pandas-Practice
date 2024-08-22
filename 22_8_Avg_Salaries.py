Compare each employee's salary with the average salary of the corresponding department.
Output the department, first name, and salary of employees along with the average salary of that department.

https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=351870476#gid=351870476


# Import your libraries
import pandas as pd

# Start writing code
dep_salary = employee.groupby('department')['salary'].mean().reset_index(name='avg_salary')
merged_ = employee.merge(dep_salary, left_on = 'department', right_on = 'department')
merged_[['department', 'first_name','salary','avg_salary']]
