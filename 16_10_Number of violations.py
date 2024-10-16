	# Import your libraries																								
	import pandas as pd																								
																									
	# Start writing code																								
	new = sf_restaurant_health_violations[(sf_restaurant_health_violations['business_name']=='Roxanne Cafe') & (sf_restaurant_health_violations['violation_id'].notnull())]																								
	new['inspection_date'] = new['inspection_date'].dt.year																								
	new.groupby('inspection_date')['violation_id'].count().reset_index()																								



https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=316997557#gid=316997557
