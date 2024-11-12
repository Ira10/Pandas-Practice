Find the review_text that received the highest number of 'cool' votes. Output the business name along with the review text with the highest numbef of 'cool' votes.									
									
	# Import your libraries								
	import pandas as pd								
									
	# Start writing code								
	max_ =  yelp_reviews['cool'].max()								
									
	yelp_reviews[yelp_reviews['cool'] == max_][['business_name','review_text']]								



https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=849693574#gid=849693574
