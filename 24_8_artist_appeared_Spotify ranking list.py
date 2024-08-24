Find how many times each artist appeared on the Spotify ranking list Output the artist name along with the corresponding number of occurrences. 		
Order records by the number of occurrences in descending order.		
		
	# Import your libraries	
	import pandas as pd	
		
	# Start writing code	
	#### no 1 ### count needs a column	
	spotify_worldwide_daily_song_ranking.groupby('artist')['id'].count() .reset_index(name='n_occurences').sort_values(by='n_occurences', ascending=False)	
		
	##### no 2 #### size doesn't need a column	
	spotify_worldwide_daily_song_ranking.groupby('artist').size().reset_index(name='n_occurences').sort_values(by='n_occurences', ascending=False)	


https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=132688843#gid=132688843
