Find libraries who haven't provided the email address in circulation year 2016 but their notice preference definition is set to email

# Import your libraries	
import pandas as pd	
	

library_usage[(library_usage['notice_preference_definition'] == 'email') & (library_usage['provided_email_address'] == False) & 
                                                            (library_usage['circulation_active_year'] == 2016)][['home_library_code']].drop_duplicates()	


https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=1143075908#gid=1143075908
