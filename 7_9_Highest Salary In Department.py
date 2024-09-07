Find the employee with the highest salary per department. Output the department name, employee's first name along with the corresponding salary.				
				
				
		# Import your libraries		
		import pandas as pd		
				
		# Start writing code		
		employee['rank'] = employee.groupby('department')['salary'].rank(method = 'dense', ascending=False)		
		employee[employee['rank']==1][['department','first_name','salary']]		
				
				
