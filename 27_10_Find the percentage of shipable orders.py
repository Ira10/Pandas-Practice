Find the percentage of shipable orders. Consider an order is shipable if the customer's address is known.	
	


	"# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(orders, customers, left_on ='cust_id', right_on ='id')


perc = df['address'].dropna().shape[0] / df.shape[0] * 100




https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=1265749388#gid=1265749388
