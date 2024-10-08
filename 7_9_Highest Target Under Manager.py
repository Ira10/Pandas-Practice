Find the highest target achieved by the employee or employees who works under the manager id 13. Output the first name of the employee and target achieved. 		
The solution should show the highest target achieved under manager_id=13 and which employee(s) achieved it.		
		

                                                                     
	# Import your libraries	
	import pandas as pd	
		
	# Start writing code	
	salesforce_employees = salesforce_employees[salesforce_employees['manager_id']==13]	
	salesforce_employees['rank'] = salesforce_employees['target'].rank(method='dense', ascending=False)	
	salesforce_employees[salesforce_employees['rank']==1][['first_name','target']]	
		
		
