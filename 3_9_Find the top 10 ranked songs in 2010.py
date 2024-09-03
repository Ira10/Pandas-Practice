"What were the top 10 ranked songs in 2010?
Output the rank, group name, and song name but do not show the same song twice.
Sort the result based on the year_rank in ascending order."					
					
# Import your libraries					
import pandas as pd					
					
# Start writing code					
billboard_top_100_year_end[billboard_top_100_year_end['year']==2010].drop_duplicates(subset=['year_rank','year'])
                             .sort_values(by='year_rank', ascending=True)[['year_rank', 'group_name','song_name']].head(10)					
					
					
billboard_top_100_year_end					
year	year_rank	group_name	artist	song_name	id
1956	1	Elvis Presley	Elvis Presley	Heartbreak Hotel	1
1956	2	Elvis Presley	Elvis Presley	Don't Be Cruel	2
