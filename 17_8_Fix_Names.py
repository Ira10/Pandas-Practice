Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase. Return the result table ordered by user_id.									


import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
users['name'] = users['name'].str.capitalize() 
result_df = users.sort_values(by='user_id', ascending=True)
return result_df



https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=298033126#gid=298033126
