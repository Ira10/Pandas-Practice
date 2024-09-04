Second Highest Salary							4th Sep																		
																									
Find the second highest salary of employees.																									
																									
																									
# Import your libraries																									
import pandas as pd																									
																									
# Start writing code																									
employee['rank'] = employee['salary'].rank(method = 'dense', ascending=False)																									
employee[employee['rank']==2][['salary']]																									
																									
																									

																									
