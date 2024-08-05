Write a query that will calculate the number of shipments per month. The unique key for one shipment is a combination of shipment_id and sub_id. 
Output the year_month in format YYYY-MM and the number of shipments in that month. (https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=1929893520#gid=1929893520)

amazon_shipment['month'] = amazon_shipment['shipment_date'].dt.strftime("%Y-%m")
amazon_shipment['unique_'] = amazon_shipment['shipment_id'].astype(str) + amazon_shipment['sub_id'].astype(str)
amazon_shipment.groupby(['month'])['unique_'].nunique().reset_index()


Output	
month	unique_
2021-08	3
2021-09	6


In case of not using reset_index()
getting only
unique_
3
6
