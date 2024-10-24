Classify each business as either a restaurant, cafe, school, or other.	
• A restaurant should have the word 'restaurant' in the business name. • A cafe should have either 'cafe', 'café', or 'coffee' in the business name. • A school should have the word 'school' in the business name. • All other businesses should be classified as 'other'.	
Output the business name and their classification.	

  https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=1244843596#gid=1244843596


Regex	
import re	
import pandas as pd	
	
def categorize_business(row):	
business_name = row['business_name'].lower()	
	
if re.search('restaurant', business_name):	
return 'restaurant'	
elif re.search('cafe|café|coffee', business_name):	
return 'cafe'	
elif re.search('school', row['business_name'].lower()):	
return 'school'	
else:	
return 'other'	
	
# Apply the function to the dataframe	
sf_restaurant_health_violations['business_type'] = sf_restaurant_health_violations.apply(categorize_business, axis=1)	
	
sf_restaurant_health_violations[['business_name','business_type']].drop_duplicates()	


222222222
import pandas as pd	
	
# Define a custom function	
def categorize_business(row):	
# Convert business_name to lowercase for case-insensitive matching	
business_name = row['business_name'].lower()	
	
if 'restaurant' in business_name:	
return 'restaurant'	
	
elif any(keyword in business_name for keyword in ['cafe', 'café', 'coffee']):	
return 'cafe'	
	
elif 'school' in business_name:	
return 'school'	
	
else:	
return 'other'	
	
# Apply the function to the dataframe	
sf_restaurant_health_violations['business_type'] = sf_restaurant_health_violations.apply(categorize_business, axis=1)	
	
sf_restaurant_health_violations[['business_name','business_type']].drop_duplicates()	
	
	
	
