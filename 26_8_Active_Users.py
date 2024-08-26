Output share of US users that are active. Active users are the ones with an "open" status in the table. 


# Import your libraries
import pandas as pd

# Start writing code
all_ = fb_active_users[fb_active_users['country'] == 'USA'].shape[0]

active_ = fb_active_users[(fb_active_users['status']=='open') & (fb_active_users['country'] == 'USA')].shape[0]
# print(all_)
# print(active_)
active_/all_


https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=1259768107#gid=1259768107
