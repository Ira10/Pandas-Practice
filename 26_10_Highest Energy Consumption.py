Find the date with the highest total energy consumption from the Meta/Facebook data centers. Output the date along with the total energy consumption across all data centers.		
		
		
When you're using groupby in pandas, the max() function does not return the overall maximum value across all groups; instead, it returns the maximum value for each group. Here’s how to clarify its usage in your context:		


	# Import your libraries	
	import pandas as pd	
		
	new_df = pd.concat([fb_eu_energy, fb_asia_energy, fb_na_energy])	
	consumption = new_df.groupby('date', as_index=False).sum()	
	consumption[consumption['consumption']==consumption['consumption'].max()][['date','consumption']]	
	# consumption.groupby('date')['consumption'].max()	
