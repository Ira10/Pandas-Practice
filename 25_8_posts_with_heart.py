Find all posts which were reacted to with a heart. For such posts output all columns from facebook_posts table.		
		
	# Import your libraries	
	import pandas as pd	
		
	# Start writing code	
	merged_ = facebook_posts.merge(facebook_reactions, left_on = ['post_id','poster'], right_on = ['post_id','poster'])	
	merged_[merged_['reaction']=='heart'][['post_id','poster','post_text','post_keywords','post_date']].drop_duplicates(subset = 'post_id')	


https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=808004612#gid=808004612
