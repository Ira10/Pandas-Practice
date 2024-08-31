User with Most Approved Flags								31st Aug																	


Which user flagged the most distinct videos that ended up approved by YouTube? Output, in one column, their full name or names in case of a tie. 																									
In the user's full name, include a space between the first and the last name.																									



	import pandas as pd																								
																									
	# Start writing code																								
	merged_ = flag_review.merge(user_flags, left_on = 'flag_id', right_on = 'flag_id')																								
	merged_['username'] = merged_['user_firstname'] + " " + merged_['user_lastname']																								
	merged_[merged_['reviewed_outcome']=='APPROVED'] 																								
	new = merged_.groupby('username')['video_id'].nunique().reset_index()																								
	new.sort_values(by ='video_id', ascending=False)[new['video_id']> 1][['username']]																								
