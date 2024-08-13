Write a solution to find the first login date for each player. Return the result table in any order.							


https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=998469260#gid=998469260



import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
# activity['event_date'] = pd.to_datetime(activity['event_date'])       # don't need this 
activity['rank'] = activity.groupby('player_id')['event_date'].rank(method='min', ascending=True)
return activity[activity['rank']==1].rename(columns={'event_date':'first_login'})[['player_id','first_login']]
