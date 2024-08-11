Find the activity date and the pe_description of facilities with the name 'STREET CHURROS' and with a score of less than 95 points.

  

# Import your libraries
import pandas as pd

# Start writing code
new = los_angeles_restaurant_health_inspections[los_angeles_restaurant_health_inspections['facility_name'].str.contains('STREET CHURROS')]
score_less_95 = new[new['score'] < 95][['activity_date','pe_description']]


https://docs.google.com/spreadsheets/d/1abXSPieLpPtnhRlpPWF7ukATxTnxNZw6mQnpTqnwT4s/edit?gid=314969347#gid=314969347
