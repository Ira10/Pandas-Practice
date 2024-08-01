Write a query that returns the number of unique users per client per month

https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=1043433579#gid=1043433579


# Import your libraries
import pandas as pd

result = fact_events.groupby([fact_events['client_id'], fact_events['time_id'].dt.month])['user_id'].nunique().reset_index()
