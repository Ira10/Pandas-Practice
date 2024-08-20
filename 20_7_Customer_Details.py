"Find the details of each customer regardless of whether the customer made an order. Output the customer's first name, last name, and the city along with the order details.
Sort records based on the customer's first name and the order details in ascending order."



# Import your libraries
import pandas as pd

# Start writing code
joined_ = customers.merge(orders, how = 'left', left_on = 'id', right_on = 'cust_id')
joined_[['first_name','last_name','city','order_details']].sort_values(by=(['first_name','order_details']), ascending=True)



https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=2133576030#gid=2133576030
