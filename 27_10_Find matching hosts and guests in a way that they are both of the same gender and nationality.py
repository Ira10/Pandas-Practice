Find matching hosts and guests pairs in a way that they are both of the same gender and nationality. Output the host id and the guest id of matched pair.		
		
		
		
	# Import your libraries	
	import pandas as pd	
		
	# Start writing code	
	df = pd.merge(airbnb_hosts,airbnb_guests, left_on =['nationality', 'gender'], right_on = ['nationality', 'gender'])[['host_id','guest_id']].drop_duplicates()	




https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=792795842#gid=792795842
