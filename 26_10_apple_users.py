https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=1804984802#gid=1804984802


import pandas as pd							26th Oct				
import numpy as np											
											
merged = pd.merge(playbook_events, playbook_users, on="user_id")											
mac_device = ["macbook pro", "iphone 5s", "ipad air"]											
df = (											
merged[merged["device"].isin(mac_device)]											
.groupby("language")["user_id"]											
.nunique()											
.to_frame("n_apple_users")											
)											
											
result = (											
merged.groupby(["language"])["user_id"]											
.nunique()											
.rename("n_total_users")											
.reset_index()											
)											
											
result.merge(df, how="outer", left_on="language", right_on="language").fillna(0).sort_values("n_total_users", ascending=False)[["language", "n_apple_users", "n_total_users"]]											
											
