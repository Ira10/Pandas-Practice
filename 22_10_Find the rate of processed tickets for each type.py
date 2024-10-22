# Import your libraries	
import pandas as pd	
	
# Start writing code	
all_ = facebook_complaints.groupby('type')['processed'].count().reset_index()	
	
proc = facebook_complaints[facebook_complaints['processed']==True]	
processed_ = proc.groupby('type')['processed'].count().reset_index()	
	
	
joined_df = all_.merge(processed_, left_on = 'type', right_on='type')	
joined_df['processed_rate']= joined_df['processed_y']/joined_df['processed_x']	
joined_df[['type','processed_rate']]	






https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=667257563#gid=667257563
