Meta/Facebook has developed a new programing language called Hack.To measure the popularity of Hack they ran a survey with their employees. 													
The survey included data on previous programing familiarity as well as the number of years of experience, age, gender and most importantly satisfaction with Hack. 													
Due to an error location data was not collected, but your supervisor demands a report showing average popularity of Hack by office location. 													
Luckily the user IDs of employees completing the surveys were stored. Based on the above, find the average popularity of the Hack per office location. Output the location along with the average popularity.													
													
													
# Import your libraries
import pandas as pd

# Start writing code
joined_ = facebook_hack_survey.merge(facebook_employees, left_on = 'employee_id', right_on = 'id')
joined_.groupby('location')['popularity'].mean().reset_index()


https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=1170982289#gid=1170982289
