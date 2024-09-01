Find the number of apartments per nationality that are owned by people under 30 years old.		
Output the nationality along with the number of apartments.  Sort records by the apartments count in descending order.	


  
		
	import pandas as pd	
		
	# Start writing code	
	airbnb_units = airbnb_units[airbnb_units['unit_type'] == 'Apartment']	
	airbnb_hosts = airbnb_hosts[airbnb_hosts['age'] < 30]	
		
	new = airbnb_units.merge(airbnb_hosts, left_on = 'host_id', right_on = 'host_id')	
	new_ = new.groupby('nationality')['unit_id'].nunique().reset_index(name='apartment_count')	
