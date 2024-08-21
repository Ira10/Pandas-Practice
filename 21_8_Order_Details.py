"Find order details made by Jill and Eva. Consider the Jill and Eva as first names of customers. Output the order date, details and cost along with the first name.
"

https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=1027840667#gid=1027840667


" # Import your libraries
import pandas as pd

# Start writing code
joined_ = customers.merge(orders, how = 'inner', left_on = 'id', right_on = 'cust_id')
joined_[(joined_['first_name']=='Jill') | (joined_['first_name']=='Eva')][['first_name','order_date', 'order_details', 'total_order_cost']] "											
First Sol


import pandas as pd											
											
joined_ = customers.merge(orders, how = 'inner', left_on = 'id', right_on = 'cust_id')											
cust = ["Jill", "Eva"]											
result = joined_[joined_["first_name"].isin(cust)][["first_name", "order_date", "order_details", "total_order_cost"]]											
Second Solution											
