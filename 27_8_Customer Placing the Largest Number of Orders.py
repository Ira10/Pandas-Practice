Write a solution to find the customer_number for the customer who has placed the largest number of orders.
The test cases are generated so that exactly one customer will have placed more orders than any other customer.



import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
     new = orders.groupby('customer_number').size().reset_index(name='count')
     new['rank'] = new['count'].rank(method='min', ascending=False)
     return new[new['rank']==1][['customer_number']]
