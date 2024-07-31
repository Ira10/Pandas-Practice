Find the base pay for Police Captains. Output the employee name along with the corresponding base pay.

link - https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=1774392128#gid=1774392128

# Import your libraries	
import pandas as pd	
	
# Start writing code	
	
result = sf_public_salaries[sf_public_salaries['jobtitle'].str.contains('POLICE')]	
result[['employeename','basepay']]	
