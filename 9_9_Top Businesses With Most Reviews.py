Top Businesses With Most Reviews						9th September 																			
																									
Find the top 5 businesses with most reviews. Assume that each row has a unique business_id such that the total reviews for each business is listed on each row. 																									
Output the business name along with the total number of reviews and order your results by the total reviews in descending order.																									
																									
# Import your libraries																									
import pandas as pd																									
																									
# Start writing code																									
yelp_business.groupby('name')['review_count'].sum().reset_index(name='review_count').sort_values(by='review_count', ascending =False)[:5]																									
																									



Output																									
name	review_count																								
Iron Chef	331																								
Jacs Dining and Tap House	197																								
Grimaldi's Pizzeria	187																								
Signs Restaurant	120																								
Kassab's	101																								
