You have been asked to find the 5 most lucrative products in terms of total revenue for the first half of 2022 (from January to June inclusive). Output their IDs and the total revenue.


# Import your libraries
import pandas as pd

# Start writing code
online_orders['rev'] = online_orders['cost_in_dollars'] * online_orders['units_sold']
online_orders = online_orders.query("date >= '2022-01-01 00:00:00' or date <= '2022-06-30 00:00:00'")
new_orders = online_orders.groupby(by = 'product_id')['rev'].sum().reset_index()
new_orders["ranking"] = new_orders['rev'].rank(method="min", ascending=False)
new_orders.rename(columns = {'rev':'total'},inplace=True)
new_orders[new_orders['ranking'] <= 5][["product_id", "total"]].sort_values(
total, ascending=False)



https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=109666512#gid=109666512
