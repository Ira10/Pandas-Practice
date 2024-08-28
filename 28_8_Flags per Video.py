For each video, find how many unique users flagged it. A unique user can be identified using the combination of their first name and last name. 	
Do not consider rows in which there is no flag ID.	


	
# Import your libraries	
import pandas as pd	
	
# Start writing code	
user_flags = user_flags[user_flags['flag_id'].notnull()]	
	
user_flags['concat_'] = user_flags['user_firstname'].astype(str) + " " + user_flags['user_lastname'].astype(str)	
	
user_flags.groupby('video_id')['concat_'].nunique().reset_index(name='num_unique_users')	
	
	
