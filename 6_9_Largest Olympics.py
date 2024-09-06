Find the Olympics with the highest number of athletes. The Olympics game is a combination of the year and the season, and is found in the 'games' column. 			
Output the Olympics along with the corresponding number of athletes.			


   
			
	# Import your libraries		
	import pandas as pd		
			
	# Start writing code		
	new_ = olympics_athletes_events.groupby('games')['name'].nunique().reset_index(name = 'athletes_count')		
	new_['rank'] = new_['athletes_count'].rank(method = 'dense', ascending=False)		
	new_[new_['rank']==1][['games','athletes_count']]		
			
