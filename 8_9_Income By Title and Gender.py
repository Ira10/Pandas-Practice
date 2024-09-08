Find the average total compensation based on employee titles and gender. Total compensation is calculated by adding both the salary and bonus of each employee. 	
However, not every employee receives a bonus so disregard employees without bonuses in your calculation. Employee can receive more than one bonus. 	
Output the employee title, gender (i.e., sex), along with the average total compensation.	


sf_employee['id'].value_counts().reset_index(name='occur')				
this is to check how many times an id is occuring, like duplicate records				
				
sf_bonus['worker_ref_id'].value_counts().reset_index(name='occur')				



import pandas as pd	
	
# Start writing code	
total_bonus = sf_bonus.groupby('worker_ref_id')['bonus'].sum().reset_index()	
new_ = total_bonus.merge(sf_employee, how = 'inner', left_on = 'worker_ref_id', right_on = 'id' )	
new_['total_comp'] = new_['bonus'] + new_['salary']	
new_.groupby(['employee_title','sex'])['total_comp'].mean().reset_index()	
