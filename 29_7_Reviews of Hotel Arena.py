https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=1336344490#gid=1336344490

Find the number of rows for each review score earned by 'Hotel Arena'. Output the hotel name (which should be 'Hotel Arena')
review score along with the corresponding number of rows with that score for the specified hotel.

# Import your libraries
import pandas as pd

# Start writing code
hotel_reviews = hotel_reviews[hotel_reviews['hotel_name'] == 'Hotel Arena']
hotel_reviews = hotel_reviews.groupby(['hotel_name', 'reviewer_score']).size().reset_index(name='n_reviews')
hotel_reviews[['reviewer_score','hotel_name','n_reviews']]
