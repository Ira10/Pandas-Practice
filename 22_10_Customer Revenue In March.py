Calculate the total revenue from each customer in March 2019. Include only customers who were active in March 2019.										
Output the revenue along with the customer id and sort the results based on the revenue in descending order.										
										
										
										
										
										
	# Import your libraries									
	import pandas as pd									
										
	# Start writing code									
	orders = orders[(orders['order_date'].dt.year == 2019) & (orders['order_date'].dt.month == 3)]									
	orders.groupby('cust_id')['total_order_cost'].sum().reset_index(name='revenue')									






https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=1424348107#gid=1424348107
