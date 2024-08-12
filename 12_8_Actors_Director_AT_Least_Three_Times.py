Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.								
Return the result table in any order.								


import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
raw = actor_director.groupby(['actor_id','director_id']).size().reset_index(name='count_')
return raw[raw['count_']>=3][['actor_id','director_id']]    ## at_least (not == 3)



https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=774755766#gid=774755766
