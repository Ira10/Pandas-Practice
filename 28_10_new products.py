https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=1820477874#gid=1820477874


You are given a table of product launches by company by year. Write a query to count the net difference between the number of products companies launched in 2020 with the number of products companies launched in the previous year. Output the name of the companies and a net difference of net products released for 2020 compared to the previous year.	
	
	
	# Import your libraries
	import pandas as pd
	
	# Start writing code
	car_20 = car_launches[car_launches['year']==2020].groupby(['year','company_name'])['product_name'].nunique().reset_index(name='net_new_products')
	
	car_19 = car_launches[car_launches['year']==2019].groupby(['year','company_name'])['product_name'].nunique().reset_index(name='net_new_products')
	new = pd.merge(car_20, car_19, on =['company_name'])
	new['net_new_products'] = new['net_new_products_x'] - new['net_new_products_y']
	new[['company_name','net_new_products']]
