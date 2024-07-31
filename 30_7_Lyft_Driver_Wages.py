Find all Lyft drivers who earn either equal to or less than 30k USD or equal to or more than 70k USD. Output all details related to retrieved records.

Link - https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=355113853#gid=355113853

# Import your libraries	
import pandas as pd	
	
# Start writing code	
filtered_drivers = lyft_drivers[(lyft_drivers['yearly_salary'] <= 30000) | (lyft_drivers['yearly_salary'] >= 70000)] ##1	
filtered_drivers	
	
	
# Assuming lyft_drivers is your DataFrame	
# filtered_drivers = lyft_drivers[(lyft_drivers['yearly_salary'] <= 30000) or (lyft_drivers['yearly_salary'] >= 70000)] or doesn't work	
	
lyft_drivers.query("yearly_salary <= 30000 or yearly_salary >= 70000") ##2	
	
lyft_drivers[~lyft_drivers.yearly_salary.between(30000, 70000)] ##3	
