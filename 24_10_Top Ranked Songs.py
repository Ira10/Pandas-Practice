Find songs that have ranked in the top position. Output the track name and the number of times it ranked at the top. Sort your records by the number of times the song was in the top position in descending order.		
		
		
		
		
	# Import your libraries	
	import pandas as pd	
		
	# Start writing code	
	spotify_worldwide_daily_song_ranking = spotify_worldwide_daily_song_ranking[spotify_worldwide_daily_song_ranking['position']==1]	
	spotify_worldwide_daily_song_ranking.groupby('trackname')['id'].count().reset_index(name='times_top1').sort_values(by='times_top1',ascending=False)	
		



https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=551543328#gid=551543328
